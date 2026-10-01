package dev.ryanhcode.sable.mixin.sublevel_render.impl.sodium;

import com.mojang.blaze3d.platform.Lighting;
import com.mojang.blaze3d.vertex.PoseStack;
import dev.ryanhcode.sable.api.client.SubLevelBlockEntityRenderRegistry;
import dev.ryanhcode.sable.api.sublevel.ClientSubLevelContainer;
import dev.ryanhcode.sable.api.sublevel.SubLevelContainer;
import dev.ryanhcode.sable.companion.math.Pose3dc;
import dev.ryanhcode.sable.mixinterface.sublevel_render.SubLevelBlockEntityRenderExtension;
import dev.ryanhcode.sable.sublevel.ClientSubLevel;
import dev.ryanhcode.sable.sublevel.plot.LevelPlot;
import dev.ryanhcode.sable.sublevel.render.SubLevelRenderData;
import dev.ryanhcode.sable.sublevel.render.SubLevelLightVertexConsumerProvider;
import it.unimi.dsi.fastutil.longs.Long2ObjectMap;
import net.caffeinemc.mods.sodium.client.render.SodiumWorldRenderer;
import net.caffeinemc.mods.sodium.client.render.chunk.ChunkRenderMatrices;
import net.caffeinemc.mods.sodium.client.render.viewport.Viewport;
import net.caffeinemc.mods.sodium.client.util.FogParameters;
import net.fabricmc.fabric.api.client.renderer.v1.Renderer;
import net.fabricmc.fabric.api.client.renderer.v1.mesh.QuadEmitter;
import net.fabricmc.fabric.api.client.renderer.v1.render.AltModelBlockRenderer;
import net.fabricmc.fabric.api.client.renderer.v1.render.ChunkSectionLayerHelper;
import net.minecraft.client.Camera;
import net.minecraft.client.Minecraft;
import net.minecraft.client.PrioritizeChunkUpdates;
import net.minecraft.client.multiplayer.ClientLevel;
import net.minecraft.client.renderer.LevelRenderer;
import net.minecraft.client.renderer.MultiBufferSource;
import net.minecraft.client.renderer.block.BlockStateModelSet;
import net.minecraft.client.renderer.block.dispatch.BlockStateModel;
import net.minecraft.client.renderer.chunk.ChunkSectionLayer;
import net.minecraft.client.renderer.chunk.ChunkSectionLayerGroup;
import net.minecraft.client.renderer.chunk.RenderRegionCache;
import net.minecraft.client.renderer.rendertype.RenderType;
import net.minecraft.client.renderer.state.level.LevelRenderState;
import net.minecraft.client.renderer.texture.OverlayTexture;
import net.minecraft.core.BlockPos;
import net.minecraft.server.level.BlockDestructionProgress;
import net.minecraft.util.LightCoordsUtil;
import net.minecraft.world.level.block.RenderShape;
import net.minecraft.world.level.block.entity.BlockEntity;
import net.minecraft.world.level.block.state.BlockState;
import org.jetbrains.annotations.Nullable;
import org.joml.Vector3dc;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.Shadow;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;

import java.util.SortedSet;

/**
 * Bridges Sable sub-levels into Sodium's terrain render phases.
 *
 * <p>The Iris/Sodium pipeline requires its own extended vertex format. Sable's
 * vanilla compiled section buffers are accepted by the GPU but discarded by that
 * shader pipeline. Render the sub-level blocks through the block-model pipeline
 * instead; Iris decorates the moving-block render types with the active
 * shader-pack vertex format just as it does for pistons.</p>
 *
 * <p>PORT-NOTE(mc26.1): the immediate block-model entry point changed shape. The
 * old FRAPI flow ({@code Renderer#render} plus a {@code BlockMultiBufferSource})
 * no longer exists; it is now a two-step flow:</p>
 * <ol>
 *   <li>{@link AltModelBlockRenderer#tesselateBlock} tessellates a
 *       {@link BlockStateModel} into {@link QuadEmitter} quads, preserving FRAPI
 *       quad extensions, and</li>
 *   <li>each emitted quad is written into the vanilla moving-block render types
 *       via {@link ChunkSectionLayerHelper#getMovingBlockRenderType}.</li>
 * </ol>
 * <p>This mirrors how Fabric API itself drives the vanilla moving-block and
 * section-compiler paths in 26.1.</p>
 */
@Mixin(value = SodiumWorldRenderer.class, remap = false)
public abstract class SodiumWorldRendererMixin {

    @Shadow
    private @Nullable ClientLevel level;

    // Sodium cancels LevelRenderer#extractVisibleBlockEntities at HEAD, which
    // bypasses Sable's vanilla RETURN hook. Append transformed plot block
    // entities after Sodium has extracted the ordinary world block entities.
    @Inject(method = "extractBlockEntities", at = @At("TAIL"))
    private void sable$extractSubLevelBlockEntities(
            final Camera camera,
            final float partialTick,
            final Long2ObjectMap<SortedSet<BlockDestructionProgress>> destructionProgress,
            final LevelRenderState levelRenderState,
            final CallbackInfo ci
    ) {
        final LevelRenderer levelRenderer = Minecraft.getInstance().levelRenderer;
        ((SubLevelBlockEntityRenderExtension) levelRenderer)
                .sable$extractSubLevelBlockEntities(camera, partialTick, levelRenderState);
    }

    @Inject(method = "setupTerrain", at = @At("TAIL"))
    private void sable$compileSubLevelSections(
            final Camera camera,
            final Viewport viewport,
            final FogParameters fogParameters,
            final boolean spectator,
            final boolean updateImmediately,
            final ChunkRenderMatrices matrices,
            final CallbackInfo ci
    ) {
        if (this.level == null) {
            return;
        }

        final ClientSubLevelContainer container = SubLevelContainer.getContainer(this.level);
        if (container == null) {
            return;
        }

        final PrioritizeChunkUpdates chunkUpdates = Minecraft.getInstance().options.prioritizeChunkUpdates().get();
        final RenderRegionCache renderRegionCache = new RenderRegionCache();
        for (final ClientSubLevel subLevel : container.getAllSubLevels()) {
            subLevel.getRenderData().compileSections(chunkUpdates, renderRegionCache, camera);
        }
    }

    @Inject(method = "scheduleRebuildForChunk", at = @At("HEAD"), cancellable = true)
    private void sable$scheduleSubLevelRebuild(
            final int sectionX,
            final int sectionY,
            final int sectionZ,
            final boolean playerChanged,
            final CallbackInfo ci
    ) {
        if (this.level == null) {
            return;
        }

        final ClientSubLevelContainer container = SubLevelContainer.getContainer(this.level);
        if (container == null) {
            return;
        }

        final LevelPlot plot = container.getPlot(sectionX, sectionZ);
        if (plot == null) {
            return;
        }

        ((ClientSubLevel) plot.getSubLevel()).getRenderData().setDirty(sectionX, sectionY, sectionZ, playerChanged);
        ci.cancel();
    }

    @Inject(method = "drawChunkLayer", at = @At("TAIL"))
    private void sable$drawSubLevelSections(
            final ChunkSectionLayerGroup group,
            final ChunkRenderMatrices matrices,
            final double cameraX,
            final double cameraY,
            final double cameraZ,
            final CallbackInfo ci
    ) {
        if (this.level == null || group != ChunkSectionLayerGroup.OPAQUE) {
            return;
        }

        final ClientSubLevelContainer container = SubLevelContainer.getContainer(this.level);
        if (container == null) {
            return;
        }

        final Minecraft minecraft = Minecraft.getInstance();
        final MultiBufferSource.BufferSource bufferSource = minecraft.renderBuffers().bufferSource();
        // 26.1 deleted BlockRenderDispatcher (and Minecraft#getBlockRenderer); the
        // block-state model table now lives on the model manager instead.
        final BlockStateModelSet blockStateModelSet = minecraft.getModelManager().getBlockStateModelSet();
        final float partialTick = minecraft.getDeltaTracker().getGameTimeDeltaPartialTick(true);

        final Renderer fabricRenderer = Renderer.get();
        final AltModelBlockRenderer modelRenderer = fabricRenderer.altModelBlockRenderer(
                minecraft.options.ambientOcclusion().get(),
                minecraft.options.cutoutLeaves().get(),
                minecraft.getBlockColors()
        );

        // This injection runs from Sodium's opaque terrain draw, just before
        // LevelRenderer normally selects the world-lighting UBO. The block model
        // pipeline consumes that UBO for directional face shading, so bind it
        // here as well instead of inheriting stale GUI/item lights.
        minecraft.gameRenderer.getLighting().setupFor(Lighting.Entry.LEVEL);

        for (final ClientSubLevel subLevel : container.getAllSubLevels()) {
            final SubLevelLightVertexConsumerProvider blockBuffers = new SubLevelLightVertexConsumerProvider(
                    this.level,
                    subLevel,
                    cameraX,
                    cameraY,
                    cameraZ,
                    bufferSource
            );
            final SubLevelRenderData renderData = subLevel.getRenderData();
            final Pose3dc renderPose = subLevel.renderPose(partialTick);
            final Vector3dc rotationPoint = renderPose.rotationPoint();
            final PoseStack poseStack = new PoseStack();
            poseStack.mulPose(renderData.getTransformation(cameraX, cameraY, cameraZ));
            final var bounds = subLevel.getPlot().getBoundingBox();
            for (final BlockPos plotPos : BlockPos.betweenClosed(
                    bounds.minX(), bounds.minY(), bounds.minZ(),
                    bounds.maxX(), bounds.maxY(), bounds.maxZ())) {
                // betweenClosed reuses one mutable position, and the emitter
                // callback below captures it, so take a stable copy.
                final BlockPos blockPos = plotPos.immutable();
                final BlockState blockState = this.level.getBlockState(blockPos);
                if (blockState.isAir()) {
                    continue;
                }

                poseStack.pushPose();
                // Subtract in double precision before storing the translation in
                // the float pose matrix; plot coordinates are tens of millions of
                // blocks away and two separate translations lose local precision.
                poseStack.translate(
                        blockPos.getX() - rotationPoint.x(),
                        blockPos.getY() - rotationPoint.y(),
                        blockPos.getZ() - rotationPoint.z()
                );
                if (blockState.getRenderShape() == RenderShape.MODEL) {
                    // The terrain-like renderer computes AO and packed light for
                    // every vertex. Passing the level plus the real plot position
                    // lets it sample the plot's light and tints, so nearby light
                    // sources never step from one sub-level block to the next.
                    final BlockStateModel blockStateModel = blockStateModelSet.get(blockState);
                    final QuadEmitter emitter = fabricRenderer.quadEmitter(quad -> {
                        if (quad.emissive()) {
                            quad.lightmap(
                                    LightCoordsUtil.FULL_BRIGHT, LightCoordsUtil.FULL_BRIGHT,
                                    LightCoordsUtil.FULL_BRIGHT, LightCoordsUtil.FULL_BRIGHT
                            );
                        }

                        final ChunkSectionLayer layer = quad.chunkLayer();
                        final RenderType renderType = ChunkSectionLayerHelper.getMovingBlockRenderType(
                                layer == null ? ChunkSectionLayer.SOLID : layer
                        );
                        // Writes all four vertices with this overlay; the pose is
                        // evaluated here, while the block translation is applied.
                        quad.buffer(
                                OverlayTexture.NO_OVERLAY,
                                poseStack.last(),
                                blockBuffers.getBuffer(renderType)
                        );
                    });
                    modelRenderer.tesselateBlock(
                            emitter,
                            0.0F,
                            0.0F,
                            0.0F,
                            this.level,
                            blockPos,
                            blockState,
                            blockStateModel,
                            blockState.getSeed(blockPos)
                    );
                }

                final BlockEntity blockEntity = this.level.getBlockEntity(blockPos);
                if (blockEntity != null && !blockEntity.isRemoved()) {
                    final int plotLight = LevelRenderer.getLightCoords(this.level, blockPos);
                    SubLevelBlockEntityRenderRegistry.render(
                            blockEntity,
                            partialTick,
                            poseStack,
                            blockBuffers,
                            plotLight,
                            OverlayTexture.NO_OVERLAY
                    );
                }
                poseStack.popPose();
            }
        }

        bufferSource.endBatch();
    }

}
