package io.github.fabricators_of_create.porting_lib.conditions;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

/**
 * Vendored stand-in for Porting Lib's {@code porting_lib.conditions.WithConditions}.
 *
 * <p>Pairs a datapack value with the conditions that must hold for it to be registered.
 *
 * <p>Adapted for 26.1: identical to upstream - the record depends on no renamed vanilla
 * types. Upstream's builder validates through {@code org.apache.commons.lang3.Validate};
 * this port uses the equivalent {@link java.util.Objects} checks to avoid depending on
 * commons-lang3 being on the compile classpath.
 *
 * @param <A> the type of the carried value
 */
public record WithConditions<A>(List<ICondition> conditions, A carrier) {

    public WithConditions(A carrier, ICondition... conditions) {
        this(List.of(conditions), carrier);
    }

    public WithConditions(A carrier) {
        this(List.of(), carrier);
    }

    /** @return a builder that produces a {@link WithConditions} for {@code carrier} */
    public static <A> Builder<A> builder(A carrier) {
        return new Builder<A>().withCarrier(carrier);
    }

    /** Builds a {@link WithConditions}, requiring at least one condition. */
    public static class Builder<T> {

        private final List<ICondition> conditions = new ArrayList<>();
        private T carrier;

        public Builder<T> addCondition(ICondition... condition) {
            this.conditions.addAll(List.of(condition));
            return this;
        }

        public Builder<T> addCondition(Collection<ICondition> conditions) {
            this.conditions.addAll(conditions);
            return this;
        }

        public Builder<T> withCarrier(T carrier) {
            this.carrier = carrier;
            return this;
        }

        public WithConditions<T> build() {
            if (this.carrier == null) {
                throw new NullPointerException("You need to supply a carrier to create a WithConditions");
            }
            if (this.conditions.isEmpty()) {
                throw new IllegalArgumentException("You need to supply at least one condition to create a WithConditions");
            }
            return new WithConditions<>(List.copyOf(this.conditions), this.carrier);
        }
    }
}
