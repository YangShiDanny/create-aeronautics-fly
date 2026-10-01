package io.github.fabricators_of_create.porting_lib.models.generators;

import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Set;
import java.util.function.Function;
import java.util.stream.Collectors;

import com.google.gson.JsonObject;

import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.level.block.state.properties.Property;

/**
 * Vendored stand-in for Porting Lib's {@code VariantBlockStateBuilder}.
 *
 * <p>Builds the {@code variants} form of a blockstate JSON file: a map from a
 * property-value selector to the model(s) to use.
 */
public class VariantBlockStateBuilder implements IGeneratedBlockState {

    private final Block owner;
    private final Map<PartialBlockstate, ConfiguredModelList> models = new LinkedHashMap<>();
    private final Set<BlockState> coveredStates = new HashSet<>();

    VariantBlockStateBuilder(Block owner) {
        this.owner = owner;
    }

    public Block getOwner() {
        return this.owner;
    }

    /** @return the selector to model mapping backing this builder */
    public Map<PartialBlockstate, ConfiguredModelList> getModels() {
        return this.models;
    }

    public ConfiguredModelList get(PartialBlockstate state) {
        return this.models.get(state);
    }

    public void setModels(PartialBlockstate state, ConfiguredModel[] models) {
        setModels(state, new BlockStateProvider.ConfiguredModelList(models));
    }

    public void setModels(PartialBlockstate state, ConfiguredModelList models) {
        if (models == null) {
            throw new NullPointerException("ConfiguredModelList must not be null");
        }
        this.models.put(state, models);
        this.coveredStates.addAll(state.getCoveredStates());
    }

    /** @return an all-wildcard selector for this block */
    public PartialBlockstate partialState() {
        return new PartialBlockstate(this.owner, new HashMap<>(), this);
    }

    /** @return a selector with the given properties pinned */
    public PartialBlockstate partialState(Map<Property<?>, Comparable<?>> values) {
        return new PartialBlockstate(this.owner, new HashMap<>(values), this);
    }

    public VariantBlockStateBuilder forAllStates(Function<BlockState, ConfiguredModel[]> mapper) {
        return forAllStatesExcept(mapper);
    }

    @SafeVarargs
    public final VariantBlockStateBuilder forAllStatesExcept(Function<BlockState, ConfiguredModel[]> mapper,
                                                             Property<?>... ignored) {
        final Set<PartialBlockstate> seen = new HashSet<>();
        for (final BlockState blockState : this.owner.getStateDefinition().getPossibleStates()) {
            final Map<Property<?>, Comparable<?>> propVals = new HashMap<>(blockState.getValues());
            for (final Property<?> p : ignored) {
                propVals.remove(p);
            }
            final PartialBlockstate state = partialState(propVals);
            if (seen.add(state)) {
                this.models.put(state, new BlockStateProvider.ConfiguredModelList(mapper.apply(blockState)));
            }
        }
        return this;
    }

    @Override
    public JsonObject toJson() {
        final JsonObject variants = new JsonObject();
        for (final Map.Entry<PartialBlockstate, ConfiguredModelList> entry : this.models.entrySet()) {
            variants.add(entry.getKey().getName(), entry.getValue().toJSON());
        }
        final JsonObject main = new JsonObject();
        main.add("variants", variants);
        return main;
    }

    /**
     * A partial blockstate: the set of property values used as a key in the
     * {@code variants} map.
     */
    public static class PartialBlockstate {

        private final Block owner;
        private final Map<Property<?>, Comparable<?>> setStates;
        private final VariantBlockStateBuilder outerBuilder;

        PartialBlockstate(Block owner, Map<Property<?>, Comparable<?>> setStates, VariantBlockStateBuilder outerBuilder) {
            this.owner = owner;
            this.setStates = setStates;
            this.outerBuilder = outerBuilder;
            for (final Comparable<?> value : setStates.values()) {
                if (value == null) {
                    throw new NullPointerException("Property value must not be null");
                }
            }
        }

        public Block getOwner() {
            return this.owner;
        }

        public VariantBlockStateBuilder getOuterBuilder() {
            return this.outerBuilder;
        }

        public Map<Property<?>, Comparable<?>> getSetStates() {
            return Map.copyOf(this.setStates);
        }

        public <T extends Comparable<T>> PartialBlockstate with(Property<T> prop, T value) {
            if (value == null) {
                throw new NullPointerException("Value must not be null");
            }
            if (this.setStates.containsKey(prop)) {
                throw new IllegalArgumentException(
                        "Property \"" + prop.getName() + "\" has already been set to " + this.setStates.get(prop));
            }
            final Map<Property<?>, Comparable<?>> newStates = new HashMap<>(this.setStates);
            newStates.put(prop, value);
            return new PartialBlockstate(this.owner, newStates, this.outerBuilder);
        }

        public ConfiguredModel.Builder<VariantBlockStateBuilder> modelForState() {
            return ConfiguredModel.builder(this.outerBuilder, this);
        }

        public PartialBlockstate setModelForState(ConfiguredModel... models) {
            if (models == null) {
                throw new NullPointerException("Models must not be null");
            }
            this.outerBuilder.setModels(this, models);
            return this;
        }

        public ConfiguredModelList getModels() {
            return this.outerBuilder.get(this);
        }

        /** @return the JSON key for this selector, e.g. {@code axis=x,encased=false} */
        public String getName() {
            return this.owner.getStateDefinition().getProperties().stream()
                    .filter(this.setStates::containsKey)
                    .map(this::propertyValueToString)
                    .collect(Collectors.joining(","));
        }

        private <T extends Comparable<T>> String propertyValueToString(Property<T> prop) {
            @SuppressWarnings("unchecked")
            final T value = (T) this.setStates.get(prop);
            return prop.getName() + "=" + prop.getName(value);
        }

        /** @return every concrete {@link BlockState} this selector matches */
        public Set<BlockState> getCoveredStates() {
            final Set<BlockState> covered = new HashSet<>();
            for (final BlockState state : this.owner.getStateDefinition().getPossibleStates()) {
                if (matches(state)) {
                    covered.add(state);
                }
            }
            return covered;
        }

        private boolean matches(BlockState state) {
            for (final Map.Entry<Property<?>, Comparable<?>> entry : this.setStates.entrySet()) {
                if (!state.hasProperty(entry.getKey()) || !state.getValue(entry.getKey()).equals(entry.getValue())) {
                    return false;
                }
            }
            return true;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) {
                return true;
            }
            if (!(o instanceof PartialBlockstate other)) {
                return false;
            }
            return this.owner == other.owner && this.setStates.equals(other.setStates);
        }

        @Override
        public int hashCode() {
            return 31 * System.identityHashCode(this.owner) + this.setStates.hashCode();
        }

        @Override
        public String toString() {
            return getName();
        }
    }
}
