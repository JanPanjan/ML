package perceptron.src.ann;

import java.util.function.Function;

public class Layer {
    private Matrix weights;
    private Matrix bias;

    private Function<Matrix, Matrix> activationFunction;

    private int layerSize;

    private Matrix lastInput;
    private Matrix lastOutput;

    public Layer(int layerSize, Function<Matrix,Matrix> activationFunction) {
        this.layerSize = layerSize;
        this.activationFunction = activationFunction;
    }

    public int initWeights(int layerSizeBefore) {
        this.weights = Matrix.randomMatrix(layerSizeBefore, layerSize);
        this.bias = Matrix.randomMatrix(1, layerSize);

        return layerSize;
    }

    public Matrix feedForoward(Matrix input) {
        lastInput = input;
        Matrix multiResult = Matrix.multiply(weights, input);
        Matrix weightedSums = Matrix.addMatrices(multiResult, bias);
        Matrix out = activationFunction.apply(weightedSums);
        lastOutput = out;
        return out;
    }

    public Matrix backPropagate(Matrix errors, float learningRate) {
        Function<Matrix, Matrix> derivative = ActivationUtils.getDerivativeFunction(this.activationFunction);

        // calculate errors for previous layer
        Matrix transposedWeights = weights.transpose();
        Matrix previousLayersErrors = Matrix.multiply(transposedWeights, errors);

        // calculate weight for learning
        Matrix outGradient = derivative.apply(lastOutput);
        Matrix errorsWithGradient = Matrix.multiplyByElement(outGradient, errors);
        Matrix biasDeltas = errorsWithGradient.multiplyScalar(learningRate);
        Matrix inputTranspose = lastInput.transpose();
        Matrix weightDeltas = Matrix.multiply(biasDeltas, inputTranspose);

        bias = Matrix.addMatrices(bias, biasDeltas);
        weights = Matrix.addMatrices(weights, weightDeltas);

        return previousLayersErrors;
    }
}
