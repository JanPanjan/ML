package perceptron.src.ann;

public class ArtificialNeuralNetwork {
    private Layer[] layers;
    private float learningRate;

    public ArtificialNeuralNetwork(int inputSize, float learningRate, Layer[] layers) {
        this.layers = layers;
        this.learningRate = learningRate;

        int sizeOfLayerBefore = inputSize;
        for (Layer layer : layers) {
            sizeOfLayerBefore = layer.initWeights(sizeOfLayerBefore);
        }
    }

    public float[] predictOne(float[] input) {
        Matrix inputMatrix = new Matrix(input).transpose();

        Matrix inputToNextLayer = inputMatrix;
        for (Layer layer : layers) {
            inputToNextLayer = layer.feedForoward(inputToNextLayer);
        }

        return inputToNextLayer.transpose().getValues()[0];
    }

    public float fitOne(float[] input, float[] targets) {
        float[] prediction = predictOne(input);
        Matrix predictionMatrix = new Matrix(prediction);
        Matrix targetMatrix = new Matrix(targets);

        Matrix errors = Matrix.subtractMatrices(targetMatrix, predictionMatrix).transpose();

        float loss = 0;
        for (float[] row : errors.getValues()) {
            for (float value : row) {
                loss += Math.abs(value);
            }
        }

        for (int i = layers.length - 1; i >= 0; i--) {
            errors = layers[i].backPropagate(errors, learningRate);
        }

        return loss;
    }
}
