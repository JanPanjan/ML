package ANN;

import java.util.function.Function;

public class Layer {
    private Matrix weights;
    private Matrix bias;
    private Function<Matrix, Matrix> activationFunction;
    private int layerSize;

    public Layer(int layerSize, Function<Matrix, Matrix> activationFunction) {
        this.activationFunction = activationFunction;
        this.layerSize = layerSize;
    }

    /**
     * Inicializira uteži.
     * @param layerSizeBefore velikost predhodnjega layerja
     * @param layerSize velikost trenutnega layerja
     */
    public int initWeights(int layerSizeBefore) {
        this.weights = Matrix.randomMatrix(layerSizeBefore, layerSize);
        this.bias = Matrix.randomMatrix(1, layerSize);
        return this.layerSize;
    }

    public Matrix feedForward(Matrix input) {
        Matrix multResult = Matrix.multiply(this.weights, input);
        Matrix weightedSums = Matrix.addMatrices(multResult, this.bias);
        Matrix out = this.activationFunction.apply(weightedSums);

        return out;
    }
}