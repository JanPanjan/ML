package perceptron.src.ann;

import java.util.function.Function;

public class ActivationUtils {
    public static Function<Matrix, Matrix> getDerivativeFunction(Function<Matrix, Matrix> activationFunction) {
        if (activationFunction == ActivationFunction.sigmoid) {
            return ActivationDerivative.sigmoid;
        }

        throw new IllegalArgumentException("Activation function not implemented");
    }
}
