/*
 * Vendored from dev.ryanhcode:sable-companion-common-1.21.1:1.6.0 (sources jar),
 * Maven: https://maven.ryanhcode.dev/releases
 *
 * 26.1.2 has no published sable-companion build, so the library is compiled from
 * source as part of the sable module. See sable/LICENSE-sable-companion.md.
 * Local changes are marked with `26.1 PORT:`.
 */
package dev.ryanhcode.sable.companion;

import dev.ryanhcode.sable.companion.math.BoundingBox3dc;
import dev.ryanhcode.sable.companion.math.Pose3dc;
import org.jetbrains.annotations.Contract;
import org.jetbrains.annotations.Nullable;

import java.util.UUID;

/**
 * Access to basic read-only sublevel info.
 *
 * @since 1.0.0
 */
public interface SubLevelAccess {

    /**
     * @return The current pose of this sub-level
     */
    @Contract(pure = true)
    Pose3dc logicalPose();

    /**
     * @return The pose of this sub-level from the previous tick
     */
    @Contract(pure = true)
    Pose3dc lastPose();

    /**
     * @return The global bounding box of this sub-level
     */
    @Contract(pure = true)
    BoundingBox3dc boundingBox();

    /**
     * The UUID of a sub-level is networked and consistent across saving/loading
     *
     * @return The UUID of this sub-level
     */
    @Contract(pure = true)
    UUID getUniqueId();

    /**
     * @return The display name of this sub-level, if present.
     */
    @Contract(pure = true)
    @Nullable String getName();

}
