package ANN;

import java.util.function.Function;

public class ActivationFunction {
    /**
     * Naredili bomo sigmoid activation function f(x) = 1 / (1 + e^-x)
     */
    public static final Function<Matrix, Matrix> sigmoid = (Matrix m) -> {
        return m.map(x -> (float) (1.f / (1.f - Math.exp(-x))));
    };

}