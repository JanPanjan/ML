package ANN;

import java.util.function.Function;

public class ActivationUtil {
    /*
     * Vrne funckijo za odvod glede na podano aktivacijsko funkcijo
     */
    public static Function<Matrix, Matrix> getDerrivative(Function<Matrix, Matrix> activationFunction) {
        if (activationFunction == ActivationFunction.sigmoid) {
            return ActivationFunction.sigmoid;
        }
        throw new IllegalArgumentException("Activation function not implemented");
    }
}
