package io.github.fabricators_of_create.porting_lib.models.generators;

import java.util.Objects;

import com.google.gson.JsonObject;

import io.github.fabricators_of_create.porting_lib.data.ExistingFileHelper;
import net.minecraft.resources.Identifier;

import org.jetbrains.annotations.Nullable;

/**
 * Vendored stand-in for Porting Lib's {@code ModelFile}.
 *
 * <p>Wraps the resource location of a model JSON file. A model file may either
 * refer to a model that is known to already exist on disk
 * ({@link ExistingModelFile}) or one whose existence is not verified
 * ({@link UncheckedModelFile}).
 *
 * <p>Adapted for 26.1: {@code ResourceLocation} is {@link Identifier}.
 */
public abstract class ModelFile {

    @Nullable
    protected Identifier location;

    protected ModelFile(@Nullable Identifier location) {
        this.location = location;
    }

    /** @return whether the referenced model JSON is known to exist */
    public abstract boolean exists();

    /** @return the location of the referenced model */
    public Identifier getLocation() {
        if (this.location == null) {
            throw new IllegalStateException("Attempted to use a ModelFile that has not been assigned a location");
        }
        return this.location;
    }

    /** @param location the new location of this model */
    protected void setLocation(Identifier location) {
        this.location = location;
    }

    /** @return the JSON body of this model */
    public abstract JsonObject toJson();

    @Override
    public String toString() {
        return "ModelFile[" + getLocation() + "]";
    }

    /**
     * A model file that is verified against the {@link ExistingFileHelper} before
     * it is used.
     */
    public static class ExistingModelFile extends ModelFile {

        private final ExistingFileHelper existingFileHelper;

        public ExistingModelFile(Identifier location, ExistingFileHelper existingFileHelper) {
            super(Objects.requireNonNull(location, "Location must not be null"));
            this.existingFileHelper = Objects.requireNonNull(existingFileHelper, "ExistingFileHelper must not be null");
        }

        @Override
        public boolean exists() {
            return this.existingFileHelper.exists(getLocation(), ExistingFileHelper.ResourceType.MODEL);
        }

        @Override
        public JsonObject toJson() {
            final JsonObject ret = new JsonObject();
            ret.addProperty("parent", getLocation().toString());
            return ret;
        }
    }

    /**
     * A model file whose existence is assumed - used to reference vanilla or
     * externally provided models such as {@code item/generated}.
     */
    public static class UncheckedModelFile extends ModelFile {

        public UncheckedModelFile(Identifier location) {
            super(location);
        }

        public UncheckedModelFile(String location) {
            this(Identifier.parse(location));
        }

        @Override
        public boolean exists() {
            return true;
        }

        @Override
        public JsonObject toJson() {
            final JsonObject ret = new JsonObject();
            ret.addProperty("parent", getLocation().toString());
            return ret;
        }
    }
}
