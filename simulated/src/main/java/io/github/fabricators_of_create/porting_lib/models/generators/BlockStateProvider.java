package io.github.fabricators_of_create.porting_lib.models.generators;

import java.nio.file.Path;
import java.util.Arrays;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.concurrent.CompletableFuture;
import java.util.function.Function;

import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;

import io.github.fabricators_of_create.porting_lib.data.ExistingFileHelper;
import net.minecraft.core.Direction;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.data.CachedOutput;
import net.minecraft.data.DataProvider;
import net.minecraft.data.PackOutput;
import net.minecraft.resources.Identifier;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.state.BlockState;

/**
 * Vendored stand-in for Porting Lib's {@code porting_lib.models.generators.BlockStateProvider}.
 *
 * <p>Generates the {@code assets/<modid>/blockstates/<block>.json} files of a mod, plus the
 * block and item models they reference, from code.
 *
 * <p>The upstream class also generates models for the full vanilla block catalogue
 * ({@code stairsBlock}, {@code slabBlock}, {@code fenceBlock}, {@code doorBlock},
 * {@code trapdoorBlock}, ...). Those helpers are large and pull in a wide slice of the
 * vanilla block hierarchy, and this port does not use them, so only the primitives that
 * the Simulated data generators actually call are provided here:
 * {@link #simpleBlock}, {@link #horizontalBlock} and {@link #directionalBlock}, plus the
 * raw {@link #getVariantBuilder} / {@link #getMultipartBuilder} entry points.
 *
 * <p>Adapted for 26.1: {@code ResourceLocation} is {@link Identifier}.
 */
public abstract class BlockStateProvider implements DataProvider {

    /** Every blockstate this provider has generated so far, keyed by its block. */
    protected final Map<Block, IGeneratedBlockState> registeredBlocks = new LinkedHashMap<>();

    private final PackOutput output;
    private final String modid;
    private final BlockModelProvider blockModels;
    private final ItemModelProvider itemModels;

    public BlockStateProvider(PackOutput output, String modid, ExistingFileHelper exFileHelper) {
        this.output = output;
        this.modid = modid;
        // The nested model providers exist so that blockstate and model generation can
        // share one ExistingFileHelper, but they must not write anything on their own -
        // run() drives them explicitly through clear()/generateAll().
        this.blockModels = new BlockModelProvider(output, modid, exFileHelper) {
            @Override
            protected void registerModels() {
            }

            @Override
            public CompletableFuture<?> run(CachedOutput cache) {
                return CompletableFuture.allOf();
            }
        };
        this.itemModels = new ItemModelProvider(output, modid, this.blockModels.existingFileHelper) {
            @Override
            protected void registerModels() {
            }

            @Override
            public CompletableFuture<?> run(CachedOutput cache) {
                return CompletableFuture.allOf();
            }
        };
    }

    @Override
    public CompletableFuture<?> run(CachedOutput cache) {
        this.models().clear();
        this.itemModels().clear();
        this.registeredBlocks.clear();
        registerStatesAndModels();
        final CompletableFuture<?>[] futures = new CompletableFuture<?>[2 + this.registeredBlocks.size()];
        int i = 0;
        futures[i++] = this.models().generateAll(cache);
        futures[i++] = this.itemModels().generateAll(cache);
        for (final Map.Entry<Block, IGeneratedBlockState> entry : this.registeredBlocks.entrySet()) {
            futures[i++] = saveBlockState(cache, entry.getValue().toJson(), entry.getKey());
        }
        return CompletableFuture.allOf(futures);
    }

    /** Fills {@link #registeredBlocks} and the model providers. */
    protected abstract void registerStatesAndModels();

    /** @return the variant-style builder for {@code b}, creating it if needed */
    public VariantBlockStateBuilder getVariantBuilder(Block b) {
        final IGeneratedBlockState old = this.registeredBlocks.get(b);
        if (old != null) {
            if (!(old instanceof VariantBlockStateBuilder)) {
                throw new IllegalStateException("Block " + b + " already has a non-variant blockstate builder");
            }
            return (VariantBlockStateBuilder) old;
        }
        final VariantBlockStateBuilder ret = new VariantBlockStateBuilder(b);
        this.registeredBlocks.put(b, ret);
        return ret;
    }

    /** @return the multipart-style builder for {@code b}, creating it if needed */
    public MultiPartBlockStateBuilder getMultipartBuilder(Block b) {
        final IGeneratedBlockState old = this.registeredBlocks.get(b);
        if (old != null) {
            if (!(old instanceof MultiPartBlockStateBuilder)) {
                throw new IllegalStateException("Block " + b + " already has a non-multipart blockstate builder");
            }
            return (MultiPartBlockStateBuilder) old;
        }
        final MultiPartBlockStateBuilder ret = new MultiPartBlockStateBuilder(b);
        this.registeredBlocks.put(b, ret);
        return ret;
    }

    /** @return the provider writing {@code models/block/} */
    public BlockModelProvider models() {
        return this.blockModels;
    }

    /** @return the provider writing {@code models/item/} */
    public ItemModelProvider itemModels() {
        return this.itemModels;
    }

    /** @return {@code name} in this provider's namespace */
    public Identifier modLoc(String name) {
        return Identifier.fromNamespaceAndPath(this.modid, name);
    }

    /** @return {@code name} in the {@code minecraft} namespace */
    public Identifier mcLoc(String name) {
        return Identifier.parse(name);
    }

    private Identifier key(Block block) {
        return BuiltInRegistries.BLOCK.getKey(block);
    }

    private String name(Block block) {
        final Identifier key = key(block);
        return key == null ? "unknown" : key.getPath();
    }

    /** @return {@code <modid>:block/<block name>}, the texture convention for simple blocks */
    public Identifier blockTexture(Block block) {
        final Identifier name = key(block);
        if (name == null) {
            throw new IllegalStateException("Cannot resolve the registry name of " + block);
        }
        return Identifier.fromNamespaceAndPath(name.getNamespace(), ModelProvider.BLOCK_FOLDER + "/" + name.getPath());
    }

    private Identifier extend(Identifier rl, String suffix) {
        return Identifier.fromNamespaceAndPath(rl.getNamespace(), rl.getPath() + suffix);
    }

    /** @return a {@code block/cube_all} model textured with {@link #blockTexture(Block)} */
    public ModelFile cubeAll(Block block) {
        return this.models().cubeAll(name(block), blockTexture(block));
    }

    /** Maps every state of {@code block} to its cube-all model. */
    public void simpleBlock(Block block) {
        simpleBlock(block, cubeAll(block));
    }

    /** Maps every state of {@code block} to the model produced by {@code expander}. */
    public void simpleBlock(Block block, Function<ModelFile, ConfiguredModel[]> expander) {
        simpleBlock(block, expander.apply(cubeAll(block)));
    }

    /** Maps every state of {@code block} to {@code model}. */
    public void simpleBlock(Block block, ModelFile model) {
        simpleBlock(block, new ConfiguredModel(model));
    }

    /** Maps every state of {@code block} to {@code models}. */
    public void simpleBlock(Block block, ConfiguredModel... models) {
        getVariantBuilder(block).partialState().setModels(models);
    }

    /** Writes a {@code model/<block>} item model with {@code model} as its parent. */
    public void simpleBlockItem(Block block, ModelFile model) {
        this.itemModels().getBuilder(key(block).getPath()).parent(model);
    }

    /** {@link #simpleBlock(Block, ModelFile)} plus its item model. */
    public void simpleBlockWithItem(Block block, ModelFile model) {
        simpleBlock(block, model);
        simpleBlockItem(block, model);
    }

    /** The rotation applied to {@code HORIZONTAL_FACING}/{@code FACING} models by default. */
    public static final int DEFAULT_ANGLE_OFFSET = 180;

    /** Maps every state of {@code block} to {@code model}, rotated by its horizontal facing. */
    public void horizontalBlock(Block block, ModelFile model) {
        horizontalBlock(block, model, DEFAULT_ANGLE_OFFSET);
    }

    /** Maps every state of {@code block} to {@code model}, rotated by its horizontal facing. */
    public void horizontalBlock(Block block, ModelFile model, int angleOffset) {
        horizontalBlock(block, $ -> model, angleOffset);
    }

    /** Maps every state of {@code block} to the model produced by {@code modelFunc}. */
    public void horizontalBlock(Block block, Function<BlockState, ModelFile> modelFunc) {
        horizontalBlock(block, modelFunc, DEFAULT_ANGLE_OFFSET);
    }

    /** Maps every state of {@code block} to {@code modelFunc}, rotated by its horizontal facing. */
    public void horizontalBlock(Block block, Function<BlockState, ModelFile> modelFunc, int angleOffset) {
        getVariantBuilder(block)
                .forAllStates(state -> ConfiguredModel.builder()
                        .modelFile(modelFunc.apply(state))
                        .rotationY(((int) state.getValue(net.minecraft.world.level.block.state.properties.BlockStateProperties.HORIZONTAL_FACING).toYRot() + angleOffset) % 360)
                        .build());
    }

    /** Maps every state of {@code block} to {@code model}, rotated by its facing. */
    public void directionalBlock(Block block, ModelFile model) {
        directionalBlock(block, model, DEFAULT_ANGLE_OFFSET);
    }

    /** Maps every state of {@code block} to {@code model}, rotated by its facing. */
    public void directionalBlock(Block block, ModelFile model, int angleOffset) {
        directionalBlock(block, $ -> model, angleOffset);
    }

    /** Maps every state of {@code block} to the model produced by {@code modelFunc}. */
    public void directionalBlock(Block block, Function<BlockState, ModelFile> modelFunc) {
        directionalBlock(block, modelFunc, DEFAULT_ANGLE_OFFSET);
    }

    /** Maps every state of {@code block} to {@code modelFunc}, rotated by its facing. */
    public void directionalBlock(Block block, Function<BlockState, ModelFile> modelFunc, int angleOffset) {
        getVariantBuilder(block)
                .forAllStates(state -> {
                    final Direction dir = state.getValue(net.minecraft.world.level.block.state.properties.BlockStateProperties.FACING);
                    return ConfiguredModel.builder()
                            .modelFile(modelFunc.apply(state))
                            .rotationX(dir == Direction.DOWN ? 180 : dir.getAxis().isHorizontal() ? 90 : 0)
                            .rotationY(dir.getAxis().isVertical() ? 0 : (((int) dir.toYRot()) + angleOffset) % 360)
                            .build();
                });
    }

    private CompletableFuture<?> saveBlockState(CachedOutput cache, JsonObject stateJson, Block owner) {
        final Identifier blockName = key(owner);
        if (blockName == null) {
            throw new IllegalStateException("Cannot resolve the registry name of " + owner);
        }
        final Path outputPath = this.output.getOutputFolder(PackOutput.Target.RESOURCE_PACK)
                .resolve(blockName.getNamespace()).resolve("blockstates").resolve(blockName.getPath() + ".json");
        return DataProvider.saveStable(cache, stateJson, outputPath);
    }

    @Override
    public String getName() {
        return "Block States: " + this.modid;
    }

    /**
     * The {@code apply} payload of a blockstate entry: a single model object, or an array
     * of weighted model entries.
     */
    public static class ConfiguredModelList {

        private final List<ConfiguredModel> models;

        private ConfiguredModelList(List<ConfiguredModel> models) {
            if (models.isEmpty()) {
                throw new IllegalArgumentException("ConfiguredModelList must not be empty");
            }
            this.models = models;
        }

        public ConfiguredModelList(ConfiguredModel model) {
            this(List.of(model));
        }

        public ConfiguredModelList(ConfiguredModel... models) {
            this(Arrays.asList(models));
        }

        /** @return either a single model object or an array of weighted models */
        public JsonElement toJSON() {
            if (this.models.size() == 1) {
                return this.models.get(0).toJSON(false);
            }
            final JsonArray ret = new JsonArray();
            for (final ConfiguredModel m : this.models) {
                ret.add(m.toJSON(true));
            }
            return ret;
        }

        /** @return a new list with {@code models} appended */
        public ConfiguredModelList append(ConfiguredModel... models) {
            final List<ConfiguredModel> all = new java.util.ArrayList<>(this.models);
            all.addAll(Arrays.asList(models));
            return new ConfiguredModelList(all);
        }
    }
}
