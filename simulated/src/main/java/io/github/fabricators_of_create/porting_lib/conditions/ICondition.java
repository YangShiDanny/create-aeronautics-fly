package io.github.fabricators_of_create.porting_lib.conditions;

import java.util.Collection;
import java.util.Map;
import java.util.Set;

import com.mojang.serialization.MapCodec;

import net.minecraft.core.Holder;
import net.minecraft.core.Registry;
import net.minecraft.resources.Identifier;
import net.minecraft.resources.ResourceKey;
import net.minecraft.tags.TagKey;

/**
 * Vendored stand-in for Porting Lib's {@code porting_lib.conditions.ICondition}.
 *
 * <p>A named predicate over resource-manager state that can be attached to recipes,
 * advancements, loot tables and the like, so that stale entries in a datapack stop
 * failing to load when the mod that owned their ingredients is absent.
 *
 * <p>The upstream interface additionally couples the condition registry and a
 * {@code ConditionalOps} codec pipeline into the type, so that conditions can be
 * codec-serialised generically. This port does not use conditions, only the two types
 * (this one and {@link WithConditions}) are named by the vendored Registrate providers,
 * so only the contract - {@link #test(IContext)} and {@link #codec()} - is declared here.
 */
public interface ICondition {

    /** @return whether this condition currently holds */
    boolean test(IContext context);

    /** @return the codec identifying this condition and carrying its arguments */
    MapCodec<? extends ICondition> codec();

    /**
     * The state a condition is evaluated against.
     *
     * <p>A context is either {@link #EMPTY} (no tag data available) or
     * {@link #TAGS_INVALID} (tag lookups are not permitted here, e.g. before the
     * resource manager has loaded).
     */
    interface IContext {

        IContext EMPTY = new IContext() {
            @Override
            public <T> Map<Identifier, Collection<Holder<T>>> getAllTags(ResourceKey<? extends Registry<T>> registry) {
                return Map.of();
            }
        };

        /**
         * A context in which tag lookups are not permitted - conditions that need tags
         * must fail loudly rather than silently evaluate to false.
         */
        IContext TAGS_INVALID = new IContext() {
            @Override
            public <T> Map<Identifier, Collection<Holder<T>>> getAllTags(ResourceKey<? extends Registry<T>> registry) {
                throw new UnsupportedOperationException("Usage of tag-based conditions is not permitted in this context!");
            }
        };

        /**
         * @param key the tag to look up
         * @return the tag's contents, or an empty collection if it is not loaded
         */
        default <T> Collection<Holder<T>> getTag(TagKey<T> key) {
            return getAllTags(key.registry()).getOrDefault(key.location(), Set.of());
        }

        /**
         * @param registry the registry to look up tags in
         * @return every loaded tag of that registry; empty if none is available
         */
        <T> Map<Identifier, Collection<Holder<T>>> getAllTags(ResourceKey<? extends Registry<T>> registry);
    }
}
