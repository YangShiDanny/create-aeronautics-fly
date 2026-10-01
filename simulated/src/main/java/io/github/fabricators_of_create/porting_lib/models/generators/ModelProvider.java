package io.github.fabricators_of_create.porting_lib.models.generators;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.concurrent.CompletableFuture;
import java.util.function.BiFunction;

import io.github.fabricators_of_create.porting_lib.data.ExistingFileHelper;
import net.minecraft.data.CachedOutput;
import net.minecraft.data.DataProvider;
import net.minecraft.data.PackOutput;
import net.minecraft.resources.Identifier;

/**
 * Vendored stand-in for Porting Lib's {@code ModelProvider}.
 *
 * <p>Collects generated models and writes each of them to
 * {@code assets/<modid>/models/<path>.json}.
 *
 * <p>Adapted for 26.1: {@code ResourceLocation} is {@link Identifier} and
 * {@code new ResourceLocation(...)} is {@code Identifier.parse(...)}.
 *
 * @param <T> the concrete builder type produced by this provider
 */
public abstract class ModelProvider<T extends ModelBuilder<T>> implements DataProvider {

    public static final String BLOCK_FOLDER = "block";
    public static final String ITEM_FOLDER = "item";

    /** Every model produced by this provider, keyed by model location. */
    public final Map<Identifier, T> generatedModels = new HashMap<>();

    /** The helper used to verify that referenced models already exist. */
    public final ExistingFileHelper existingFileHelper;

    protected final PackOutput output;
    protected final String modid;
    private final String name;
    private final PackOutput.PathProvider modelPathProvider;
    private final String folder;
    private final BiFunction<Identifier, ExistingFileHelper, T> factory;

    protected ModelProvider(PackOutput output, String modid, String folder,
                            BiFunction<Identifier, ExistingFileHelper, T> factory,
                            ExistingFileHelper existingFileHelper) {
        this.output = output;
        this.modid = modid;
        this.folder = folder;
        this.factory = factory;
        this.name = "Model Definitions with folder \"" + folder + "\"";
        this.existingFileHelper = existingFileHelper;
        this.modelPathProvider = output.createPathProvider(PackOutput.Target.RESOURCE_PACK, "models");
    }

    /** @return the folder under {@code models/} this provider writes into */
    public String getFolder() {
        return this.folder;
    }

    /** @return a new builder registered under {@code path} */
    public T getBuilder(String path) {
        final Identifier location = extendWithFolder(path.contains(":") ? Identifier.parse(path) : modLoc(path));
        if (this.generatedModels.containsKey(location)) {
            throw new IllegalStateException("Duplicate model generated: " + location);
        }
        final T ret = this.factory.apply(location, this.existingFileHelper);
        this.generatedModels.put(location, ret);
        return ret;
    }

    private Identifier extendWithFolder(Identifier loc) {
        if (loc.getPath().contains("/")) {
            return loc;
        }
        return Identifier.fromNamespaceAndPath(loc.getNamespace(), this.folder + "/" + loc.getPath());
    }

    /** @return an {@link Identifier} in this provider's namespace */
    public Identifier modLoc(String name) {
        return Identifier.fromNamespaceAndPath(this.modid, name);
    }

    /** @return an {@link Identifier} in the {@code minecraft} namespace */
    public Identifier mcLoc(String name) {
        return name.contains(":") ? Identifier.parse(name) : Identifier.withDefaultNamespace(name);
    }

    public T withExistingParent(String name, String parent) {
        return getBuilder(name).parent(parent);
    }

    public T withExistingParent(String name, Identifier parent) {
        return getBuilder(name).parent(parent);
    }

    /**
     * @param path the location of an already existing model
     * @return a model file pointing at it
     */
    public ModelFile.ExistingModelFile getExistingFile(Identifier path) {
        final ModelFile.ExistingModelFile ret = new ModelFile.ExistingModelFile(path, this.existingFileHelper);
        if (this.existingFileHelper.isEnabled() && !ret.exists()) {
            throw new IllegalStateException("Could not find existing model " + path);
        }
        return ret;
    }

    /** @return an unchecked model file reference (existence is not verified) */
    public ModelFile.UncheckedModelFile modLocUnchecked(String name) {
        return new ModelFile.UncheckedModelFile(modLoc(name));
    }

    /** Called once per run to register every model this provider owns. */
    protected abstract void registerModels();

    /** Drops all previously generated models so a new run can rebuild them. */
    public void clear() {
        this.generatedModels.clear();
    }

    /** Writes every registered model to disk. */
    public CompletableFuture<?> generateAll(CachedOutput cache) {
        final List<CompletableFuture<?>> futures = new ArrayList<>();
        for (final Map.Entry<Identifier, T> entry : this.generatedModels.entrySet()) {
            futures.add(DataProvider.saveStable(cache, entry.getValue().toJson(),
                    this.modelPathProvider.json(entry.getKey())));
        }
        return CompletableFuture.allOf(futures.toArray(CompletableFuture[]::new));
    }

    @Override
    public String getName() {
        return this.name;
    }

    @Override
    public CompletableFuture<?> run(CachedOutput cache) {
        registerModels();
        return generateAll(cache);
    }
}
