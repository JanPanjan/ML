package ANN;

// ANN oz. v našem primeru MLP (multi-layered preceptron)
public class ArtificialNeuralNetwork {
    private Layer[] layers;
    private float learningRate;

    public ArtificialNeuralNetwork(int inputSize, float learningRate, Layer[] layers) {
        this.layers = layers;
        this.learningRate = learningRate;

        // za vsak layer inicializiramo weights
        int sizeOfLayerBefore = inputSize;

        // wtf to je tok smart
        for (Layer layer : this.layers) {
            sizeOfLayerBefore = layer.initWeights(sizeOfLayerBefore);
        }
    }

    /**
     * Predvidi verjetnosti za vsak input.
     * @param input seznam naših input vrednosti
     * @return seznam float vrednosti
     */
    public float[] predictOne(float[] input) {
        Matrix inputMatrix = new Matrix(input).transpose();
        Matrix inputToNextLayer = inputMatrix;

        for (Layer layer : this.layers) {
            inputToNextLayer = layer.feedForward(inputToNextLayer);
        }

        // baje vrne dvojni array [[...]]
        return inputToNextLayer.transpose().getValues()[0];
    }

    /**
     * 
     * @param input 
     * @param targets pravilne vrednosti
     */
    public void fitOne(float[] input, float[] targets) {
        // naredi napoved glede na input
        float[] predictions = predictOne(input);

        Matrix predictionMatrix = new Matrix(predictions);
        Matrix targetsnMatrix = new Matrix(targets);

        // Od targets ošteje predictions, zračuna končni error
        Matrix errors = Matrix.subtractMatrices(targetsnMatrix, predictionMatrix).transpose();

        for (int i = layers.length - 1; i >= 0; i--) {
            errors = layers[i].backPropagate(errors, this.learningRate);
        }
    }
}
