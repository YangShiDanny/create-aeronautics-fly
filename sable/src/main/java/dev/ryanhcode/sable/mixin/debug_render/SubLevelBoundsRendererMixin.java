package dev.ryanhcode.sable.mixin.debug_render;

import dev.ryanhcode.sable.api.sublevel.SubLevelContainer;
import dev.ryanhcode.sable.companion.math.BoundingBox3dc;
import dev.ryanhcode.sable.companion.math.BoundingBox3ic;
import dev.ryanhcode.sable.companion.math.Pose3dc;
import dev.ryanhcode.sable.network.client.ClientSableInterpolationState;
import dev.ryanhcode.sable.network.client.SubLevelSnapshotInterpolator;
import dev.ryanhcode.sable.sublevel.ClientSubLevel;
import dev.ryanhcode.sable.sublevel.SubLevel;
import net.minecraft.client.Minecraft;
import net.minecraft.client.gui.components.debug.DebugScreenEntries;
import net.minecraft.client.renderer.culling.Frustum;
import net.minecraft.client.renderer.debug.DebugRenderer;
import net.minecraft.gizmos.GizmoStyle;
import net.minecraft.gizmos.Gizmos;
import net.minecraft.util.ARGB;
import net.minecraft.world.phys.AABB;
import net.minecraft.world.phys.Vec3;
import org.joml.Matrix4f;
import org.joml.Matrix4fc;
import org.joml.Quaternionf;
import org.joml.Vector3d;
import org.joml.Vector3dc;
import org.joml.Vector3f;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.Unique;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;

/**
 * Draws sub-level bounding boxes in the F3+B debug pass.
 *
 * <p>PORT-NOTE(mc26.1): the debug pipeline was rewritten around "gizmos".
 * {@code DebugRenderer#render(PoseStack, Frustum, BufferSource, double, double,
 * double, boolean)} no longer exists - it is now
 * {@link DebugRenderer#emitGizmos(Frustum, double, double, double, float)}, and
 * geometry is produced through the world-space {@link Gizmos} helpers instead of
 * an immediate {@code VertexConsumer}. Consequently there is no {@code PoseStack}
 * to rotate a box with; the rotated plot bounds are emitted as explicit line
 * segments with their corners pushed through the sub-level transform.</p>
 */
@Mixin(DebugRenderer.class)
public class SubLevelBoundsRendererMixin {

    /**
     * The 12 edges of a unit cube, indexing the corner order produced by
     * {@link #sable$corners} ({@code 4 * x + 2 * y + z}).
     */
    @Unique
    private static final int[][] SABLE_BOX_EDGES = {
            {0, 1}, {2, 3}, {4, 5}, {6, 7},
            {0, 2}, {1, 3}, {4, 6}, {5, 7},
            {0, 4}, {1, 5}, {2, 6}, {3, 7}
    };

    @Inject(method = "emitGizmos", at = @At("TAIL"))
    private void sable$emitSubLevelBounds(
            final Frustum frustum,
            final double cameraX,
            final double cameraY,
            final double cameraZ,
            final float partialTick,
            final CallbackInfo ci
    ) {
        final Minecraft minecraft = Minecraft.getInstance();

        if (minecraft.showOnlyReducedInfo()
                || !minecraft.debugEntries.isCurrentlyEnabled(DebugScreenEntries.ENTITY_HITBOXES)
                || minecraft.level == null) {
            return;
        }

        final SubLevelContainer container = SubLevelContainer.getContainer(minecraft.level);
        if (container == null) {
            return;
        }

        for (final SubLevel subLevel : container.getAllSubLevels()) {
            if (!(subLevel instanceof final ClientSubLevel clientSubLevel)) {
                continue;
            }

            final BoundingBox3dc bounds = subLevel.boundingBox();
            Gizmos.cuboid(
                    new AABB(
                            bounds.minX(), bounds.minY(), bounds.minZ(),
                            bounds.maxX(), bounds.maxY(), bounds.maxZ()
                    ),
                    GizmoStyle.stroke(ARGB.colorFromFloat(0.7f, 0.5f, 0.5f, 0.5f))
            );

            final Pose3dc renderPose = clientSubLevel.renderPose();
            final Vector3dc globalCenter = renderPose.position();
            final Vector3dc rotationPoint = renderPose.rotationPoint();

            // Marker cube around the rotation point, 4/16 of a block wide.
            Gizmos.cuboid(
                    AABB.ofSize(
                            new Vec3(globalCenter.x(), globalCenter.y(), globalCenter.z()),
                            4.0 / 16.0, 4.0 / 16.0, 4.0 / 16.0
                    ),
                    GizmoStyle.stroke(ARGB.colorFromFloat(1.0f, 0.7f, 0.7f, 0.5f))
            );

            // The plot is axis-aligned in plot space, so its bounds have to be
            // rotated into world space by the sub-level orientation. Plot-local
            // coordinates are measured from the rotation point.
            final BoundingBox3ic plotBounds = subLevel.getPlot().getBoundingBox();
            final Matrix4f plotToWorld = new Matrix4f()
                    .translate((float) globalCenter.x(), (float) globalCenter.y(), (float) globalCenter.z())
                    .rotate(new Quaternionf(renderPose.orientation()));

            sable$emitBox(
                    plotToWorld,
                    plotBounds.minX() - rotationPoint.x(),
                    plotBounds.minY() - rotationPoint.y(),
                    plotBounds.minZ() - rotationPoint.z(),
                    plotBounds.maxX() + 1.0 - rotationPoint.x(),
                    plotBounds.maxY() + 1.0 - rotationPoint.y(),
                    plotBounds.maxZ() + 1.0 - rotationPoint.z(),
                    ARGB.colorFromFloat(1.0f, 0.9f, 0.5f, 0.5f)
            );

            if (ClientSableInterpolationState.RENDER_INTERPOLATION_BOUNDS) {
                final Vector3d boundSize = bounds.size(new Vector3d());
                final SubLevelSnapshotInterpolator interpolator = clientSubLevel.getInterpolator();

                for (final SubLevelSnapshotInterpolator.Snapshot snapshot : interpolator.buffer) {
                    final Vector3dc center = snapshot.pose().position();

                    Gizmos.cuboid(
                            AABB.ofSize(
                                    new Vec3(center.x(), center.y(), center.z()),
                                    boundSize.x, boundSize.y, boundSize.z
                            ),
                            GizmoStyle.stroke(ARGB.colorFromFloat(0.5f, 0.0f, 1.0f, 1.0f))
                    );
                }
            }
        }
    }

    /**
     * Emits the 12 wireframe edges of a box given in a local frame, transformed
     * into world space by {@code transform}. Gizmos are world-space, so the
     * corners have to be transformed by hand.
     */
    @Unique
    private static void sable$emitBox(
            final Matrix4fc transform,
            final double minX,
            final double minY,
            final double minZ,
            final double maxX,
            final double maxY,
            final double maxZ,
            final int color
    ) {
        final Vector3f[] corners = sable$corners(transform, minX, minY, minZ, maxX, maxY, maxZ);

        for (final int[] edge : SABLE_BOX_EDGES) {
            final Vector3f from = corners[edge[0]];
            final Vector3f to = corners[edge[1]];
            Gizmos.line(new Vec3(from.x, from.y, from.z), new Vec3(to.x, to.y, to.z), color);
        }
    }

    @Unique
    private static Vector3f[] sable$corners(
            final Matrix4fc transform,
            final double minX,
            final double minY,
            final double minZ,
            final double maxX,
            final double maxY,
            final double maxZ
    ) {
        final Vector3f[] corners = new Vector3f[8];
        int index = 0;

        for (int x = 0; x < 2; x++) {
            for (int y = 0; y < 2; y++) {
                for (int z = 0; z < 2; z++) {
                    corners[index++] = transform.transformPosition(new Vector3f(
                            (float) (x == 0 ? minX : maxX),
                            (float) (y == 0 ? minY : maxY),
                            (float) (z == 0 ? minZ : maxZ)
                    ));
                }
            }
        }

        return corners;
    }
}
