package io.github.fabricators_of_create.porting_lib.models.generators;

import io.github.fabricators_of_create.porting_lib.data.ExistingFileHelper;
import net.minecraft.data.PackOutput;
import net.minecraft.resources.Identifier;

/**
 * Vendored stand-in for Porting Lib's {@code ItemModelProvider}.
 *
 * <p>A {@link ModelProvider} that writes into {@code models/item/}.
 */
public abstract class ItemModelProvider extends ModelProvider<ItemModelBuilder> {

    public ItemModelProvider(PackOutput output, String modid, ExistingFileHelper existingFileHelper) {
        super(output, modid, ITEM_FOLDER, ItemModelBuilder::new, existingFileHelper);
    }

    /** @return an {@code item/generated} model with {@code layer0} set to {@code texture} */
    public ItemModelBuilder singleTexture(String name, Identifier parent, Identifier texture) {
        return singleTexture(name, parent, "layer0", texture);
    }

    /** @return a model with {@code parent} and a single texture entry */
    public ItemModelBuilder singleTexture(String name, Identifier parent, String textureKey, Identifier texture) {
        return getBuilder(name).parent(parent).texture(textureKey, texture);
    }
}
