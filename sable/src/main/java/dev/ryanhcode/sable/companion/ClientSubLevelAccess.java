/*
 * Vendored from dev.ryanhcode:sable-companion-common-1.21.1:1.6.0 (sources jar),
 * Maven: https://maven.ryanhcode.dev/releases
 *
 * 26.1.2 has no published sable-companion build, so the library is compiled from
 * source as part of the sable module. See sable/LICENSE-sable-companion.md.
 * Local changes are marked with `26.1 PORT:`.
 */
package dev.ryanhcode.sable.companion;

import dev.ryanhcode.sable.companion.math.Pose3dc;
import org.jetbrains.annotations.Contract;

/**
 * @since 1.0.0
 */
public interface ClientSubLevelAccess extends SubLevelAccess {

    /**
     * @return The pose used for sub-level rendering with the current frame partial-tick
     */
    @Contract(pure = true)
    Pose3dc renderPose();

    /**
     * @return The pose used for sub-level rendering with a particular partial-tick
     */
    @Contract(pure = true)
    Pose3dc renderPose(float partialTick);

}
