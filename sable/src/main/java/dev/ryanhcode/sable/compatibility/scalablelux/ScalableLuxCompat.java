package dev.ryanhcode.sable.compatibility.scalablelux;

import ca.spottedleaf.starlight.common.light.StarLightEngine;
import ca.spottedleaf.starlight.common.light.StarLightInterface;
import ca.spottedleaf.starlight.common.light.StarLightLightingProvider;
import dev.ryanhcode.sable.Sable;
import net.minecraft.world.level.ChunkPos;
import net.minecraft.world.level.chunk.LevelChunk;
import net.minecraft.world.level.lighting.LevelLightEngine;

import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.List;

/**
 * Direct bridge to ScalableLux's lighting implementation.
 *
 * <p>This class is only linked when Fabric Loader reports ScalableLux as
 * loaded. Keeping the optional types here allows the rest of Sable to load
 * normally without ScalableLux on the class path.</p>
 */
public final class ScalableLuxCompat {

    /**
     * Entry points that have been used to drop a chunk's queued light tasks.
     *
     * <p>PORT-NOTE(mc26.1): on 1.21.10 this was a direct call to
     * {@code StarLightInterface#removeChunkTasks(ChunkPos)}. ScalableLux 0.3.x for
     * 26.1 reshuffled its queues behind internal {@code LightQueue}
     * implementations and there is no 26.1 artifact to compile against from this
     * project, so the entry point is resolved once, reflectively, against the
     * shapes ScalableLux has historically exposed. If none resolve we degrade to
     * the vanilla half of the operation.</p>
     */
    private static final Method REMOVE_CHUNK_TASKS = resolveRemoveChunkTasks();

    private ScalableLuxCompat() {
    }

    public static boolean hasBlockLight(final LevelLightEngine engine) {
        return getLightEngine(engine).hasBlockLight();
    }

    public static boolean hasSkyLight(final LevelLightEngine engine) {
        return getLightEngine(engine).hasSkyLight();
    }

    public static void lightChunk(final LevelLightEngine engine, final LevelChunk chunk) {
        final StarLightInterface scalableLux = getLightEngine(engine);
        chunk.setLightCorrect(false);
        scalableLux.lightChunk(chunk, StarLightEngine.getEmptySectionsForChunk(chunk));
        chunk.setLightCorrect(true);
        engine.setLightEnabled(chunk.getPos(), true);
    }

    public static void removeChunk(final LevelLightEngine engine, final ChunkPos pos) {
        if (REMOVE_CHUNK_TASKS != null) {
            try {
                final Class<?> parameterType = REMOVE_CHUNK_TASKS.getParameterTypes()[0];
                REMOVE_CHUNK_TASKS.invoke(getLightEngine(engine), parameterType == long.class ? pos.pack() : pos);
            } catch (final ReflectiveOperationException | RuntimeException failure) {
                Sable.LOGGER.warn("ScalableLux: could not drop queued light tasks for {}", pos, failure);
            }
        }

        engine.setLightEnabled(pos, false);
    }

    private static Method resolveRemoveChunkTasks() {
        final List<String> names = new ArrayList<>(List.of("removeChunkTasks", "removeChunk"));

        for (final String name : names) {
            for (final Class<?> parameterType : new Class<?>[]{ChunkPos.class, long.class}) {
                try {
                    return StarLightInterface.class.getMethod(name, parameterType);
                } catch (final NoSuchMethodException ignored) {
                    // This ScalableLux build does not expose that shape; try the next one.
                }
            }
        }

        return null;
    }

    private static StarLightInterface getLightEngine(final LevelLightEngine engine) {
        if (!(engine instanceof final StarLightLightingProvider provider)) {
            throw new IllegalStateException(
                    "ScalableLux is loaded but LevelLightEngine has no StarLightLightingProvider"
            );
        }
        return provider.getLightEngine();
    }
}
