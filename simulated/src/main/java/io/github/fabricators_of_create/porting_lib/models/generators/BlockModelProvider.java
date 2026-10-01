package io.github.fabricators_of_create.porting_lib.models.generators;

import io.github.fabricators_of_create.porting_lib.data.ExistingFileHelper;
import net.minecraft.data.PackOutput;
import net.minecraft.resources.Identifier;

/**
 * Vendored stand-in for Porting Lib's {@code BlockModelProvider}.
 *
 * <p>A {@link ModelProvider} that writes into {@code models/block/}.
 */
public abstract class BlockModelProvider extends ModelProvider<BlockModelBuilder> {

    public BlockModelProvider(PackOutput output, String modid, ExistingFileHelper existingFileHelper) {
        super(output, modid, BLOCK_FOLDER, BlockModelBuilder::new, existingFileHelper);
    }

    /** @return a {@code block/cube_all} model using {@code texture} for every face */
    public BlockModelBuilder cubeAll(String name, Identifier texture) {
        return getBuilder(name).parent(mcLoc("block/cube_all")).texture("all", texture);
    }
}
