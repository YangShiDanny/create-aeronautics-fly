package io.github.fabricators_of_create.porting_lib.tags;

import net.minecraft.core.registries.Registries;
import net.minecraft.resources.Identifier;
import net.minecraft.tags.TagKey;
import net.minecraft.world.item.Item;

/**
 * Vendored stand-in for Porting Lib's {@code porting_lib.tags.Tags}.
 *
 * <p>Porting Lib re-exports the {@code c} (common) and {@code neoforge} tag namespaces so
 * that code written against NeoForge's conventions keeps working on Fabric. The upstream
 * class declares several hundred tag constants across {@code Blocks}, {@code Items},
 * {@code Fluids}, {@code Enchantments}, {@code Biomes}, {@code Structures} and
 * {@code DamageTypes}.
 *
 * <p>Only the members this port actually references are declared here; the rest would be
 * unreferenced declarations. Add more as the port needs them - the pattern is uniformly
 * {@code TagKey.create(Registries.<REGISTRY>, Identifier.fromNamespaceAndPath("c", name))}.
 *
 * <p>Adapted for 26.1: {@code ResourceLocation} is {@link Identifier}.
 */
public class Tags {

    /** Common ({@code c}) item tags. */
    public static class Items {

        /** Every kind of wooden rod, regardless of wood type. */
        public static final TagKey<Item> RODS_WOODEN = tag("rods/wooden");

        private static TagKey<Item> tag(String name) {
            return TagKey.create(Registries.ITEM, Identifier.fromNamespaceAndPath("c", name));
        }

        private static TagKey<Item> neoforgeTag(String name) {
            return TagKey.create(Registries.ITEM, Identifier.fromNamespaceAndPath("neoforge", name));
        }
    }
}
