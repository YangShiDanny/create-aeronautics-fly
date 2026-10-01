package io.github.fabricators_of_create.porting_lib.data;

import java.nio.file.Path;
import java.util.Map;
import java.util.TreeMap;
import java.util.concurrent.CompletableFuture;
import java.util.function.Supplier;

import com.google.gson.JsonObject;

import net.minecraft.data.CachedOutput;
import net.minecraft.data.DataProvider;
import net.minecraft.data.PackOutput;
import net.minecraft.resources.Identifier;
import net.minecraft.resources.ResourceKey;
import net.minecraft.tags.TagKey;
import net.minecraft.world.effect.MobEffect;
import net.minecraft.world.entity.EntityType;
import net.minecraft.world.item.Item;
import net.minecraft.world.level.Level;
import net.minecraft.world.level.block.Block;

/**
 * Vendored stand-in for Porting Lib's {@code porting_lib.data.LanguageProvider}.
 *
 * <p>Writes {@code assets/<modid>/lang/<locale>.json} from code, with one helper per
 * kind of translatable object.
 *
 * <p>Adapted for 26.1: {@code ResourceLocation} is {@link Identifier} and
 * {@code ResourceKey#location()} is {@code ResourceKey#identifier()}. The
 * {@code ItemStack} overloads are dropped: {@code ItemStack} no longer exposes
 * {@code getDescriptionId()} - callers should resolve the id from the stack's item.
 */
public abstract class LanguageProvider implements DataProvider {

    String TRANSLATION_PREFIX = "dimension";

    private final Map<String, String> data = new TreeMap<>();
    private final PackOutput output;
    private final String modid;
    private final String locale;

    public LanguageProvider(PackOutput output, String modid, String locale) {
        this.output = output;
        this.modid = modid;
        this.locale = locale;
    }

    /** Fills in every translation this provider owns. */
    protected abstract void addTranslations();

    @Override
    public CompletableFuture<?> run(CachedOutput cache) {
        addTranslations();

        if (!this.data.isEmpty()) {
            return save(cache, this.output.getOutputFolder(PackOutput.Target.RESOURCE_PACK)
                    .resolve(this.modid).resolve("lang").resolve(this.locale + ".json"));
        }

        return CompletableFuture.allOf();
    }

    @Override
    public String getName() {
        return "Languages: " + this.locale + " for mod: " + this.modid;
    }

    private CompletableFuture<?> save(CachedOutput cache, Path target) {
        final JsonObject json = new JsonObject();
        this.data.forEach(json::addProperty);
        return DataProvider.saveStable(cache, json, target);
    }

    public void addBlock(Supplier<? extends Block> key, String name) {
        add(key.get(), name);
    }

    public void add(Block key, String name) {
        add(key.getDescriptionId(), name);
    }

    public void addItem(Supplier<? extends Item> key, String name) {
        add(key.get(), name);
    }

    public void add(Item key, String name) {
        add(key.getDescriptionId(), name);
    }

    public void addEffect(Supplier<? extends MobEffect> key, String name) {
        add(key.get(), name);
    }

    public void add(MobEffect key, String name) {
        add(key.getDescriptionId(), name);
    }

    public void addEntityType(Supplier<? extends EntityType<?>> key, String name) {
        add(key.get(), name);
    }

    public void add(EntityType<?> key, String name) {
        add(key.getDescriptionId(), name);
    }

    public void addTag(Supplier<? extends TagKey<?>> key, String name) {
        add(key.get(), name);
    }

    public void add(TagKey<?> tagKey, String name) {
        add(getTagTranslationKey(tagKey), name);
    }

    public void add(String key, String value) {
        if (this.data.put(key, value) != null) {
            throw new IllegalStateException("Duplicate translation key " + key);
        }
    }

    public void addDimension(ResourceKey<Level> dimension, String value) {
        add(dimension.identifier().toLanguageKey(TRANSLATION_PREFIX), value);
    }

    /** @return the {@code tag.<registry>.<namespace>.<path>} key for {@code tagKey} */
    public static String getTagTranslationKey(TagKey<?> tagKey) {
        final StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append("tag.");

        final Identifier registryIdentifier = tagKey.registry().registry();
        final Identifier tagIdentifier = tagKey.location();

        stringBuilder.append(registryIdentifier.toShortLanguageKey().replace("/", "."))
                .append(".")
                .append(tagIdentifier.getNamespace())
                .append(".")
                .append(tagIdentifier.getPath().replace("/", "."));

        return stringBuilder.toString();
    }
}
