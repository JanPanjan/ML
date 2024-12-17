package perceptron.src.ann;

import java.util.function.Function;

public class ActivationDerivative {
    public static final Function<Matrix, Matrix> sigmoid = (Matrix m) -> {
        return m.map(x -> x * (1.f-x));
    };
}
