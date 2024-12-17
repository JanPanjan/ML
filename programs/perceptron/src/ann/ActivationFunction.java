package perceptron.src.ann;

import java.util.function.Function;

public class ActivationFunction {
    public static final Function<Matrix,Matrix> sigmoid = (Matrix m) -> {
        return m.map(x -> (float) (1.f / (1.f + Math.exp(-x))));
    };
}
