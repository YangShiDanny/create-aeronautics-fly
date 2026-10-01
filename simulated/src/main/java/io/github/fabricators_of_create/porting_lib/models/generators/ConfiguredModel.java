package io.github.fabricators_of_create.porting_lib.models.generators;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.function.Function;

import com.google.gson.JsonArray;
import com.google.gson.JsonObject;

import org.jetbrains.annotations.Nullable;

/**
 * Vendored stand-in for Porting Lib's {@code ConfiguredModel}.
 *
 * <p>A model together with the rotation, uv-lock flag and random weight used when
 * it is referenced from a blockstate JSON file.
 *
 * <p>Adapted for 26.1: {@code BlockModelRotation#by(int, int)} no longer exists, so
 * rotation validity is checked arithmetically (multiples of 90 within
 * {@code [0, 360)}), which is the same constraint the old lookup enforced.
 */
public final class ConfiguredModel {

    /** The default random weight of configured models. */
    public static final int DEFAULT_WEIGHT = 1;

    public final ModelFile model;
    public final int rotationX;
    public final int rotationY;
    public final boolean uvLock;
    public final int weight;

    public ConfiguredModel(ModelFile model, int rotationX, int rotationY, boolean uvLock, int weight) {
        if (model == null) {
            throw new NullPointerException("Model must not be null");
        }
        this.model = model;
        checkRotation(rotationX, rotationY);
        this.rotationX = rotationX;
        this.rotationY = rotationY;
        this.uvLock = uvLock;
        checkWeight(weight);
        this.weight = weight;
    }

    public ConfiguredModel(ModelFile model, int rotationX, int rotationY, boolean uvLock) {
        this(model, rotationX, rotationY, uvLock, DEFAULT_WEIGHT);
    }

    public ConfiguredModel(ModelFile model) {
        this(model, 0, 0, false);
    }

    static void checkRotation(int rotationX, int rotationY) {
        if (!isValidRotation(rotationX, rotationY)) {
            throw new IllegalArgumentException("Invalid model rotation x=" + rotationX + ", y=" + rotationY);
        }
    }

    private static boolean isValidRotation(int rotationX, int rotationY) {
        return rotationX % 90 == 0 && rotationY % 90 == 0;
    }

    static void checkWeight(int weight) {
        if (weight <= 0) {
            throw new IllegalArgumentException("Model weight must be positive, was " + weight);
        }
    }

    /** @return the blockstate JSON object for this model */
    public JsonObject toJSON(boolean includeWeight) {
        final JsonObject ret = new JsonObject();
        ret.addProperty("model", this.model.getLocation().toString());
        if (this.rotationX != 0) {
            ret.addProperty("x", this.rotationX);
        }
        if (this.rotationY != 0) {
            ret.addProperty("y", this.rotationY);
        }
        if (this.uvLock) {
            ret.addProperty("uvlock", true);
        }
        if (includeWeight && this.weight != DEFAULT_WEIGHT) {
            ret.addProperty("weight", this.weight);
        }
        return ret;
    }

    public static Builder<?> builder() {
        return new Builder<>(null, List.of());
    }

    public static Builder<VariantBlockStateBuilder> builder(VariantBlockStateBuilder outer,
                                                           VariantBlockStateBuilder.PartialBlockstate state) {
        return new Builder<>(models -> outer.setModels(state, models), List.of());
    }

    public static Builder<MultiPartBlockStateBuilder.PartBuilder> builder(MultiPartBlockStateBuilder outer) {
        return new Builder<>(models -> {
            final MultiPartBlockStateBuilder.PartBuilder ret =
                    outer.new PartBuilder(new BlockStateProvider.ConfiguredModelList(models));
            outer.addPart(ret);
            return ret;
        }, List.of());
    }

    /**
     * A builder for {@link ConfiguredModel}s.
     *
     * @param <T> the type returned by {@link #addModel()}, supplied by the callback
     */
    public static class Builder<T> {

        @Nullable
        private ModelFile model;
        @Nullable
        private final Function<ConfiguredModel[], T> callback;
        private final List<ConfiguredModel> otherModels;
        private int rotationX;
        private int rotationY;
        private boolean uvLock;
        private int weight = DEFAULT_WEIGHT;

        Builder(@Nullable Function<ConfiguredModel[], T> callback, List<ConfiguredModel> otherModels) {
            this.callback = callback;
            this.otherModels = otherModels;
        }

        public Builder<T> modelFile(ModelFile model) {
            if (model == null) {
                throw new NullPointerException("Model must not be null");
            }
            this.model = model;
            return this;
        }

        public Builder<T> rotationX(int value) {
            checkRotation(value, this.rotationY);
            this.rotationX = value;
            return this;
        }

        public Builder<T> rotationY(int value) {
            checkRotation(this.rotationX, value);
            this.rotationY = value;
            return this;
        }

        public Builder<T> uvLock(boolean value) {
            this.uvLock = value;
            return this;
        }

        public Builder<T> weight(int value) {
            checkWeight(value);
            this.weight = value;
            return this;
        }

        public ConfiguredModel buildLast() {
            if (this.model == null) {
                throw new NullPointerException("Model must not be null");
            }
            return new ConfiguredModel(this.model, this.rotationX, this.rotationY, this.uvLock, this.weight);
        }

        public ConfiguredModel[] build() {
            final List<ConfiguredModel> all = new ArrayList<>(this.otherModels);
            all.add(buildLast());
            return all.toArray(new ConfiguredModel[0]);
        }

        public T addModel() {
            if (this.callback == null) {
                throw new NullPointerException("Cannot use addModel() without an owning builder present");
            }
            return this.callback.apply(build());
        }

        public Builder<T> nextModel() {
            return new Builder<>(this.callback,
                    List.copyOf(Arrays.asList(build())));
        }
    }
}
