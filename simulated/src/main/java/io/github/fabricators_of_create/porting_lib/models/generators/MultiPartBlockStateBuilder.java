package io.github.fabricators_of_create.porting_lib.models.generators;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import com.google.common.collect.Multimap;
import com.google.common.collect.MultimapBuilder;
import com.google.gson.JsonArray;
import com.google.gson.JsonObject;

import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.state.properties.Property;

/**
 * Vendored stand-in for Porting Lib's {@code MultiPartBlockStateBuilder}.
 *
 * <p>Builds the {@code multipart} form of a blockstate JSON file: a list of parts,
 * each with an optional {@code when} condition block and an {@code apply} list of
 * models.
 */
public final class MultiPartBlockStateBuilder implements IGeneratedBlockState {

    private final List<PartBuilder> parts = new ArrayList<>();
    private final Block owner;

    public MultiPartBlockStateBuilder(Block owner) {
        this.owner = owner;
    }

    /**
     * Starts a new part.
     *
     * @return a model builder whose {@link ConfiguredModel.Builder#addModel()} creates
     *         and registers the part
     */
    public ConfiguredModel.Builder<PartBuilder> part() {
        return ConfiguredModel.builder(this);
    }

    public MultiPartBlockStateBuilder addPart(PartBuilder part) {
        this.parts.add(part);
        return this;
    }

    @Override
    public JsonObject toJson() {
        final JsonArray variants = new JsonArray();
        for (final PartBuilder part : this.parts) {
            variants.add(part.toJson());
        }
        final JsonObject main = new JsonObject();
        main.add("multipart", variants);
        return main;
    }

    /** A single {@code multipart} entry. */
    public class PartBuilder {

        public BlockStateProvider.ConfiguredModelList models;
        public boolean useOr;
        public final Multimap<Property<?>, Comparable<?>> conditions =
                MultimapBuilder.linkedHashKeys().arrayListValues().build();
        public final List<ConditionGroup> nestedConditionGroups = new ArrayList<>();

        public PartBuilder(BlockStateProvider.ConfiguredModelList models) {
            this.models = models;
        }

        /** Makes this part apply when <em>any</em> condition is true instead of all. */
        public PartBuilder useOr() {
            this.useOr = true;
            return this;
        }

        @SafeVarargs
        public final <T extends Comparable<T>> PartBuilder condition(Property<T> prop, T... values) {
            if (prop == null) {
                throw new NullPointerException("Property must not be null");
            }
            if (values == null) {
                throw new NullPointerException("Value list must not be null");
            }
            if (values.length == 0) {
                throw new IllegalArgumentException("Value list must not be empty");
            }
            if (this.conditions.containsKey(prop)) {
                throw new IllegalArgumentException("Cannot set condition for property \"" + prop.getName() + "\" more than once");
            }
            if (!canApplyTo(this.owner)) {
                throw new IllegalArgumentException("Property " + prop + " is not valid for the block " + this.owner);
            }
            if (!this.nestedConditionGroups.isEmpty()) {
                throw new IllegalStateException("Can't have normal conditions if there are already nested condition groups");
            }
            this.conditions.putAll(prop, Arrays.asList(values));
            return this;
        }

        public final ConditionGroup nestedGroup() {
            if (!this.conditions.isEmpty()) {
                throw new IllegalStateException("Can't have nested condition groups if there are already normal conditions");
            }
            final ConditionGroup group = new ConditionGroup();
            this.nestedConditionGroups.add(group);
            return group;
        }

        public MultiPartBlockStateBuilder end() {
            return MultiPartBlockStateBuilder.this;
        }

        JsonObject toJson() {
            final JsonObject out = new JsonObject();
            if (!this.conditions.isEmpty()) {
                out.add("when", toJson(this.conditions, this.useOr));
            } else if (!this.nestedConditionGroups.isEmpty()) {
                out.add("when", toJsonNested(this.nestedConditionGroups, this.useOr));
            }
            out.add("apply", this.models.toJSON());
            return out;
        }

        public boolean canApplyTo(Block b) {
            return b.getStateDefinition().getProperties().containsAll(this.conditions.keySet());
        }

        /** A nested AND/OR group of conditions. */
        public class ConditionGroup {

            public final Multimap<Property<?>, Comparable<?>> conditions =
                    MultimapBuilder.linkedHashKeys().arrayListValues().build();
            public final List<ConditionGroup> nestedConditionGroups = new ArrayList<>();
            public boolean useOr;

            @SafeVarargs
            public final <T extends Comparable<T>> ConditionGroup condition(Property<T> prop, T... values) {
                if (!this.nestedConditionGroups.isEmpty()) {
                    throw new IllegalStateException("Can't have normal conditions if there are already nested condition groups");
                }
                this.conditions.putAll(prop, Arrays.asList(values));
                return this;
            }

            public ConditionGroup nestedGroup() {
                if (!this.conditions.isEmpty()) {
                    throw new IllegalStateException("Can't have nested condition groups if there are already normal conditions");
                }
                final ConditionGroup group = new ConditionGroup();
                this.nestedConditionGroups.add(group);
                return group;
            }

            public ConditionGroup useOr() {
                this.useOr = true;
                return this;
            }

            public PartBuilder endNestedGroup() {
                return PartBuilder.this;
            }

            public PartBuilder end() {
                return PartBuilder.this;
            }
        }
    }

    private static JsonObject toJson(Multimap<Property<?>, Comparable<?>> conditions, boolean useOr) {
        final JsonObject result = new JsonObject();
        for (final var entry : conditions.asMap().entrySet()) {
            final JsonArray values = new JsonArray();
            for (final Comparable<?> value : entry.getValue()) {
                values.add(propertyValueToString(entry.getKey(), value));
            }
            if (useOr) {
                result.add(entry.getKey().getName(), values.size() == 1 ? values.get(0) : values);
            } else {
                result.add(entry.getKey().getName(), values.size() == 1 ? values.get(0) : values);
            }
        }
        return result;
    }

    private static JsonObject toJsonNested(List<PartBuilder.ConditionGroup> groups, boolean useOr) {
        final JsonArray array = new JsonArray();
        for (final PartBuilder.ConditionGroup group : groups) {
            if (!group.conditions.isEmpty()) {
                array.add(toJson(group.conditions, group.useOr));
            } else if (!group.nestedConditionGroups.isEmpty()) {
                array.add(toJsonNested(group.nestedConditionGroups, group.useOr));
            }
        }
        final JsonObject result = new JsonObject();
        result.add(useOr ? "OR" : "AND", array);
        return result;
    }

    @SuppressWarnings("unchecked")
    private static <T extends Comparable<T>> String propertyValueToString(Property<T> property, Comparable<?> value) {
        return property.getName((T) value);
    }
}
