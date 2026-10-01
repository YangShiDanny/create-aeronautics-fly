package dev.ryanhcode.sable.mixin.sublevel_render.impl.vanilla;

import com.mojang.blaze3d.buffers.GpuBuffer;
import com.mojang.blaze3d.buffers.GpuBufferSlice;
import com.mojang.blaze3d.systems.RenderPass;
import com.mojang.blaze3d.systems.RenderSystem;
import com.mojang.blaze3d.vertex.VertexFormat;
import dev.ryanhcode.sable.Sable;
import dev.ryanhcode.sable.api.sublevel.ClientSubLevelContainer;
import dev.ryanhcode.sable.api.sublevel.SubLevelContainer;
import dev.ryanhcode.sable.mixinterface.plot.SubLevelContainerHolder;
import dev.ryanhcode.sable.platform.SableLoaderPlatform;
import dev.ryanhcode.sable.sublevel.ClientSubLevel;
import dev.ryanhcode.sable.sublevel.render.SubLevelRenderData;
import dev.ryanhcode.sable.sublevel.render.dispatcher.SubLevelRenderDispatcher;
import dev.ryanhcode.sable.sublevel.render.vanilla.VanillaChunkedSubLevelRenderData;
import it.unimi.dsi.fastutil.ints.Int2ObjectOpenHashMap;
import net.minecraft.client.Camera;
import net.minecraft.client.Minecraft;
import net.minecraft.client.PrioritizeChunkUpdates;
import net.minecraft.client.multiplayer.ClientLevel;
import net.minecraft.client.renderer.DynamicUniforms;
import net.minecraft.client.renderer.LevelRenderer;
import net.minecraft.client.renderer.chunk.ChunkSectionLayer;
import net.minecraft.client.renderer.chunk.ChunkSectionsToRender;
import net.minecraft.client.renderer.chunk.CompiledSectionMesh;
import net.minecraft.client.renderer.chunk.RenderRegionCache;
import net.minecraft.client.renderer.chunk.SectionMesh;
import net.minecraft.client.renderer.chunk.SectionRenderDispatcher;
import net.minecraft.client.renderer.culling.Frustum;
import net.minecraft.core.BlockPos;
import net.minecraft.core.SectionPos;
import net.minecraft.util.Util;
import net.minecraft.util.profiling.ProfilerFiller;
import net.minecraft.world.phys.Vec3;
import org.jetbrains.annotations.Nullable;
import org.joml.Matrix4f;
import org.joml.Matrix4fc;
import org.joml.Vector3dc;
import org.spongepowered.asm.mixin.Final;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.Shadow;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfoReturnable;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.EnumMap;
import java.util.List;


@Mixin(value = LevelRenderer.class, priority = 1002)
public abstract class LevelRendererMixin {

    @Shadow
    private @Nullable ClientLevel level;

    @Shadow
    @Final
    private Minecraft minecraft;

    @Inject(method = "compileSections", at = @At("TAIL"))
    private void sable$compileSections(final Camera camera, final CallbackInfo ci) {
        final Iterable<ClientSubLevel> sublevels = ((ClientSubLevelContainer) ((SubLevelContainerHolder) this.level).sable$getPlotContainer()).getAllSubLevels();
        final RenderRegionCache renderRegionCache = new RenderRegionCache();
        final PrioritizeChunkUpdates chunkUpdates = Minecraft.getInstance().options.prioritizeChunkUpdates().get();

        for (final ClientSubLevel sublevel : sublevels) {
            sublevel.getRenderData().compileSections(chunkUpdates, renderRegionCache, camera);
        }
    }

    @Inject(method = "cullTerrain", at = @At("HEAD"))
    public void sable$cull(final Camera camera, final Frustum frustum, final boolean spectator, final CallbackInfo ci) {
        final SubLevelRenderDispatcher dispatcher = SubLevelRenderDispatcher.get();
        dispatcher.preRenderChunks(camera);

        final ProfilerFiller profiler = net.minecraft.util.profiling.Profiler.get();
        profiler.push("sub_level_section_occlusion_graph");

        final Iterable<ClientSubLevel> sublevels = ((ClientSubLevelContainer) ((SubLevelContainerHolder) this.level).sable$getPlotContainer()).getAllSubLevels();
        final Vec3 cameraPosition = camera.position();
        dispatcher.updateCulling(sublevels, cameraPosition.x, cameraPosition.y, cameraPosition.z, frustum, spectator);

        profiler.pop();
    }

    /**
     * Appends every sub-level section to vanilla's prepared draw groups.
     *
     * <p>mc26.1: {@code SectionBuffers} and {@code LevelRenderer#prepareChunkRenders}'s
     * camera parameters are gone. The method now takes only the model-view matrix,
     * and a section's buffers are resolved through
     * {@link SectionRenderDispatcher#getRenderSectionSlice} /
     * {@link SectionMesh#getSectionDraw}. Each vanilla section also carries its own
     * {@link DynamicUniforms.ChunkSectionInfo}, so a sub-level section can supply a
     * rotated model-view without touching the vanilla ones.</p>
     */
    @Inject(method = "prepareChunkRenders", at = @At("RETURN"), cancellable = true)
    private void sable$appendSubLevelSections(final Matrix4fc baseModelView, final CallbackInfoReturnable<ChunkSectionsToRender> cir) {
        // Sodium cancels the vanilla renderGroup implementation. Its dedicated
        // mixin renders sub-level meshes after each Sodium terrain group instead.
        if (SableLoaderPlatform.INSTANCE.isModLoaded("sodium")) {
            return;
        }

        if (this.level == null) {
            return;
        }

        final ClientSubLevelContainer container = SubLevelContainer.getContainer(this.level);
        if (container == null) {
            return;
        }

        final ChunkSectionsToRender original = cir.getReturnValue();
        final Camera camera = this.minecraft.gameRenderer.getMainCamera();
        // PORT-NOTE(mc26.1): Camera#getPosition() was renamed Camera#position().
        final Vec3 cameraPosition = camera.position();

        final int atlasWidth = original.textureView().getWidth(0);
        final int atlasHeight = original.textureView().getHeight(0);
        final long visibilityMillis = Util.getMillis();

        // Vanilla keys each layer's inner map by an index into chunkSectionInfos(),
        // so appended sub-level entries must be numbered after the vanilla ones.
        final int baseInfoIndex = original.chunkSectionInfos().length;
        final List<DynamicUniforms.ChunkSectionInfo> appendedInfos = new ArrayList<>();

        final EnumMap<ChunkSectionLayer, Int2ObjectOpenHashMap<List<RenderPass.Draw<GpuBufferSlice[]>>>> drawsPerLayer = new EnumMap<>(ChunkSectionLayer.class);
        for (final ChunkSectionLayer layer : ChunkSectionLayer.values()) {
            final Int2ObjectOpenHashMap<List<RenderPass.Draw<GpuBufferSlice[]>>> existingDraws = original.drawGroupsPerLayer().get(layer);
            drawsPerLayer.put(layer, existingDraws == null ? new Int2ObjectOpenHashMap<>() : new Int2ObjectOpenHashMap<>(existingDraws));
        }

        int maxIndicesRequired = original.maxIndicesRequired();

        // Sub-level render data compiles through this same dispatcher (see
        // VanillaSubLevelRenderDispatcher), so the uber-buffer slices resolve.
        final SectionRenderDispatcher dispatcher = this.minecraft.levelRenderer.getSectionRenderDispatcher();
        dispatcher.lock();

        try {
            for (final ClientSubLevel subLevel : container.getAllSubLevels()) {
                if (!(subLevel.getRenderData() instanceof final VanillaChunkedSubLevelRenderData renderData)) {
                    continue;
                }

                final Matrix4f modelView = new Matrix4f(baseModelView).mul(
                        renderData.getTransformation(cameraPosition.x, cameraPosition.y, cameraPosition.z)
                );
                final Vector3dc rotationPoint = subLevel.renderPose().rotationPoint();

                for (final SectionRenderDispatcher.RenderSection section : renderData.allRenderSections()) {
                    final SectionMesh mesh = section.getSectionMesh();
                    if (mesh == null || mesh == CompiledSectionMesh.UNCOMPILED || mesh == CompiledSectionMesh.EMPTY) {
                        continue;
                    }

                    final BlockPos origin = section.getRenderOrigin();
                    // Section vertices are section-local and the model-view maps
                    // rotation-point-relative plot space into the world, so the
                    // offset has to be plot-local rather than the raw origin.
                    final int offsetX = origin.getX() - (int) rotationPoint.x();
                    final int offsetY = origin.getY() - (int) rotationPoint.y();
                    final int offsetZ = origin.getZ() - (int) rotationPoint.z();
                    final float visibility = section.getVisibility(visibilityMillis);

                    for (final ChunkSectionLayer layer : ChunkSectionLayer.values()) {
                        final SectionMesh.SectionDraw sectionDraw = mesh.getSectionDraw(layer);
                        if (sectionDraw == null) {
                            continue;
                        }

                        final SectionRenderDispatcher.RenderSectionBufferSlice slice = dispatcher.getRenderSectionSlice(mesh, layer);
                        final GpuBuffer indexBuffer = sectionDraw.hasCustomIndexBuffer() ? slice.indexBuffer() : null;
                        if (indexBuffer == null) {
                            // Drawn from the shared sequential index buffer, so it
                            // has to be large enough for this section too.
                            maxIndicesRequired = Math.max(maxIndicesRequired, sectionDraw.indexCount());
                        }

                        final int infoIndex = baseInfoIndex + appendedInfos.size();
                        appendedInfos.add(new DynamicUniforms.ChunkSectionInfo(
                                modelView,
                                offsetX,
                                offsetY,
                                offsetZ,
                                visibility,
                                atlasWidth,
                                atlasHeight
                        ));

                        final VertexFormat.IndexType indexType = sectionDraw.indexType();
                        drawsPerLayer.get(layer)
                                .computeIfAbsent(infoIndex, key -> new ArrayList<>())
                                .add(new RenderPass.Draw<>(
                                        0,
                                        slice.vertexBuffer(),
                                        indexBuffer,
                                        indexType,
                                        (int) (slice.indexBufferOffset() / indexType.bytes),
                                        sectionDraw.indexCount(),
                                        (int) (slice.vertexBufferOffset() / layer.vertexFormat().getVertexSize()),
                                        (transforms, uploader) -> uploader.upload("ChunkSection", transforms[infoIndex])
                                ));
                    }
                }
            }
        } finally {
            dispatcher.unlock();
        }

        if (appendedInfos.isEmpty()) {
            // Nothing to add: leave vanilla's ChunkSectionsToRender untouched.
            return;
        }

        final GpuBufferSlice[] appended = RenderSystem.getDynamicUniforms()
                .writeChunkSections(appendedInfos.toArray(DynamicUniforms.ChunkSectionInfo[]::new));
        final GpuBufferSlice[] combinedInfos = Arrays.copyOf(original.chunkSectionInfos(), baseInfoIndex + appended.length);
        System.arraycopy(appended, 0, combinedInfos, baseInfoIndex, appended.length);

        cir.setReturnValue(new ChunkSectionsToRender(original.textureView(), drawsPerLayer, maxIndicesRequired, combinedInfos));
    }

    // PORT-NOTE(mc26.1): LevelRenderer#isSectionCompiled was renamed
    // isSectionCompiledAndVisible; the old name no longer resolves as a target.
    @Inject(method = "isSectionCompiledAndVisible", at = @At("HEAD"), cancellable = true)
    private void sable$isSectionCompiled(final BlockPos blockPos, final CallbackInfoReturnable<Boolean> cir) {
        final ClientSubLevelContainer container = SubLevelContainer.getContainer(this.level);

        if (container == null) {
            return;
        }

        if (container.inBounds(blockPos)) {
            final ClientSubLevel subLevel = (ClientSubLevel) Sable.HELPER.getContaining(this.level, blockPos);

            if (subLevel == null) {
                cir.setReturnValue(false);
            } else {
                final SubLevelRenderData renderData = subLevel.getRenderData();
                final SectionPos sectionPos = SectionPos.of(blockPos);
                cir.setReturnValue(renderData.isSectionCompiled(sectionPos.x(), sectionPos.y(), sectionPos.z()));
            }
        }
    }

}
