package io.github.fabricators_of_create.porting_lib.models.generators;

import java.util.LinkedHashMap;
import java.util.Map;

import com.google.gson.JsonObject;

import io.github.fabricators_of_create.porting_lib.data.ExistingFileHelper;
import net.minecraft.resources.Identifier;

import org.jetbrains.annotations.Nullable;

/**
 * Vendored stand-in for Porting Lib's {@code ModelBuilder}.
 *
 * <p>Builds the JSON body of a model file: an optional {@code parent}, a texture
 * map, an optional {@code render_type}, and optional per-model metadata.
 *
 * <p>Only the parent/texture/render-type surface is provided. Porting Lib's
 * element/face geometry builders are omitted because this project builds all of
 * its geometry from hand-authored JSON under {@code src/main/resources} and only
 * uses the generators for the {@code parent} + {@code textures} shell.
 *
 * <p>Adapted for 26.1: {@code ResourceLocation} is {@link Identifier}.
 *
 * @param <T> the concrete builder type, for fluent chaining
 */
public class ModelBuilder<T extends ModelBuilder<T>> extends ModelFile {

    @Nullable
    protected Identifier parent;

    protected final Map<String, String> textures = new LinkedHashMap<>();

    @Nullable
    protected String renderType;

    @Nullable
    protected Boolean ambientOcclusion;

    protected final ExistingFileHelper existingFileHelper;

    protected ModelBuilder(Identifier location, ExistingFileHelper existingFileHelper) {
        super(location);
        this.existingFileHelper = existingFileHelper;
    }

    @SuppressWarnings("unchecked")
    protected T self() {
        return (T) this;
    }

    /** @param parent the parent model */
    public T parent(ModelFile parent) {
        if (parent == null) {
            throw new NullPointerException("Parent model must not be null");
        }
        this.parent = parent.getLocation();
        return self();
    }

    /** @param parent the location of the parent model */
    public T parent(String parent) {
        if (parent == null) {
            throw new NullPointerException("Parent model must not be null");
        }
        this.parent = parent.contains(":") ? Identifier.parse(parent) : Identifier.withDefaultNamespace(parent);
        return self();
    }

    /** @param texture the texture location for layer {@code key} */
    public T texture(String key, Identifier texture) {
        if (key == null) {
            throw new NullPointerException("Texture key must not be null");
        }
        if (texture == null) {
            throw new NullPointerException("Texture must not be null");
        }
        this.textures.put(key, texture.toString());
        return self();
    }

    /** @param texture the raw texture reference for layer {@code key} */
    public T texture(String key, String texture) {
        if (key == null) {
            throw new NullPointerException("Texture key must not be null");
        }
        if (texture == null) {
            throw new NullPointerException("Texture must not be null");
        }
        this.textures.put(key, texture);
        return self();
    }

    /** @param renderType the {@code render_type} value, e.g. {@code minecraft:cutout} */
    public T renderType(String renderType) {
        this.renderType = renderType;
        return self();
    }

    public T renderType(Identifier renderType) {
        return renderType(renderType.toString());
    }

    public T ao(boolean ambientOcclusion) {
        this.ambientOcclusion = ambientOcclusion;
        return self();
    }

    @Override
    public boolean exists() {
        return this.existingFileHelper.exists(getLocation(), ExistingFileHelper.ResourceType.MODEL);
    }

    @Override
    public JsonObject toJson() {
        final JsonObject root = new JsonObject();
        if (this.parent != null) {
            root.addProperty("parent", this.parent.toString());
        }
        if (this.ambientOcclusion != null) {
            root.addProperty("ambientocclusion", this.ambientOcclusion);
        }
        if (this.renderType != null) {
            root.addProperty("render_type", this.renderType);
        }
        if (!this.textures.isEmpty()) {
            final JsonObject tex = new JsonObject();
            this.textures.forEach(tex::addProperty);
            root.add("textures", tex);
        }
        return root;
    }
}
