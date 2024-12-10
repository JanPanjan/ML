package ANN;

import java.util.function.Function;

public class Layer {
    private Matrix weights;
    private Matrix bias;
    private Function<Matrix, Matrix> activationFunction;
    private int layerSize;
    private Matrix lastInput;
    private Matrix lastOutput;

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
        lastInput = input;

        Matrix multResult = Matrix.multiply(this.weights, input);
        Matrix weightedSums = Matrix.addMatrices(multResult, this.bias);
        Matrix output = this.activationFunction.apply(weightedSums);

        lastInput = output;

        return output;
    }

    public Matrix backPropagate(Matrix errors, float learningRate) {
        Function<Matrix, Matrix> derrivate = ActivationUtil.getDerrivative(this.activationFunction);

        // zračuna errors za layer pred nami (mi smo layer)
        Matrix transposeWeights = this.weights.transpose();
        Matrix previousLayerErrors = Matrix.multiply(transposeWeights, errors);

        // zračuna weight deltas za učenje
        Matrix outGradient = derrivate.apply(this.lastOutput);
        Matrix errorsWithGradient = Matrix.multiplyByElement(outGradient, errors);
        Matrix biasDeltas = errorsWithGradient.multiplyScalar(learningRate);
        Matrix inputTranspose = this.lastInput.transpose();
        Matrix weightDeltas = Matrix.multiply(biasDeltas, inputTranspose);

        this.bias = Matrix.addMatrices(this.bias, biasDeltas);
        this.weights = Matrix.addMatrices(this.weights, weightDeltas);

        return previousLayerErrors;
    }
}