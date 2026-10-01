package io.github.fabricators_of_create.porting_lib.data;

import java.io.File;
import java.nio.file.Path;
import java.util.Collection;
import java.util.Set;

import net.minecraft.resources.Identifier;
import net.minecraft.server.packs.PackType;

import org.jetbrains.annotations.Nullable;

/**
 * Vendored stand-in for Porting Lib's {@code porting_lib.data.ExistingFileHelper}.
 *
 * <p>Porting Lib used this to answer "does this model/texture already exist?" while
 * generating data, so generators could fail fast on typos. The upstream version
 * builds a {@code MultiPackResourceManager} out of the client and server packs.
 *
 * <p>This port keeps the constructor signature and the {@code exists} contract but
 * answers permissively when the helper is disabled - which is how
 * {@code SimulatedDataGenerator} constructs it
 * ({@code new ExistingFileHelper(List.of(), Set.of(), false, null, null)}).
 * Disabled means "do not verify", which is the behaviour the generators relied on.
 *
 * <p>Adapted for 26.1: {@code ResourceLocation} is {@link Identifier}.
 */
public class ExistingFileHelper {

    /** The kind of generated resource being looked up. */
    public static class ResourceType {

        public static final ResourceType MODEL = new ResourceType(PackType.CLIENT_RESOURCES, ".json", "models");
        public static final ResourceType TEXTURE = new ResourceType(PackType.CLIENT_RESOURCES, ".png", "textures");
        public static final ResourceType BLOCKSTATE = new ResourceType(PackType.CLIENT_RESOURCES, ".json", "blockstates");
        public static final ResourceType RECIPE = new ResourceType(PackType.SERVER_DATA, ".json", "recipes");

        private final PackType packType;
        private final String suffix;
        private final String prefix;

        public ResourceType(PackType packType, String suffix, String prefix) {
            this.packType = packType;
            this.suffix = suffix;
            this.prefix = prefix;
        }

        public PackType getPackType() {
            return this.packType;
        }

        public String getSuffix() {
            return this.suffix;
        }

        public String getPrefix() {
            return this.prefix;
        }
    }

    private final boolean enable;

    public ExistingFileHelper(Collection<Path> existingPacks, Set<String> existingMods, boolean enable,
                              @Nullable String assetIndex, @Nullable File assetsDir) {
        this.enable = enable;
    }

    /** @return whether existence checks are actually performed */
    public boolean isEnabled() {
        return this.enable;
    }

    /**
     * @param loc  the resource to look for
     * @param type the kind of resource
     * @return whether the resource exists - always {@code true} when disabled
     */
    public boolean exists(Identifier loc, ResourceType type) {
        return !this.enable;
    }

    public boolean exists(Identifier loc, PackType packType) {
        return !this.enable;
    }

    public boolean exists(Identifier loc, PackType packType, String pathSuffix, String pathPrefix) {
        return !this.enable;
    }
}
