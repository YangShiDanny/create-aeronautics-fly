package io.github.fabricators_of_create.porting_lib.models.generators;

import io.github.fabricators_of_create.porting_lib.data.ExistingFileHelper;
import net.minecraft.resources.Identifier;

/** Vendored stand-in for Porting Lib's {@code ItemModelBuilder}. */
public class ItemModelBuilder extends ModelBuilder<ItemModelBuilder> {

    public ItemModelBuilder(Identifier location, ExistingFileHelper existingFileHelper) {
        super(location, existingFileHelper);
    }
}
