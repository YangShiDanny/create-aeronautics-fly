package io.github.fabricators_of_create.porting_lib.models.generators;

import com.google.gson.JsonObject;

/**
 * Vendored stand-in for Porting Lib's {@code IGeneratedBlockState}.
 *
 * <p>A generated blockstate (either a variant list or a multipart list) that can
 * be serialised to its blockstate JSON form.
 */
public interface IGeneratedBlockState {

    /** @return the JSON representation written to {@code assets/<modid>/blockstates/<name>.json} */
    JsonObject toJson();
}
