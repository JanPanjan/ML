package ANN;

import java.util.function.Function;

public class ActivationDerrivative {
    /*
     * Odvod sigmoid activation funkcije f'(x) = f(x) × (1 - f(x))
     */
    public static final Function<Matrix, Matrix> sigmoid = (Matrix m) -> {
        return m.map(x -> x * (1.f - x));
    };
}
