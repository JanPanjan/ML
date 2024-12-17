package perceptron.src;

import java.util.Random;

public class Perceptron {
    float[] weights;
    float bias;
    float learningRate;

    public Perceptron(int inputSize, float learningRate) {
        this.learningRate = learningRate;
        weights = new float[inputSize];
        Random r = new Random();

        for (int i = 0; i < inputSize; i++) {
            weights[i] = r.nextFloat(-1,1);
        }
        bias = r.nextFloat(-1,1);
    }

    public float predictOne(float[] inputs) {
        float sum = weightedSum(inputs);
        return stepActivationFun(sum);
    }

    public void fitOne(float[] inputs, float correct) {
        float guess = predictOne(inputs);
        float error = correct - guess;
        for (int i = 0; i < weights.length; i++) {
            weights[i] += inputs[i] * error * learningRate;
        }
        bias += 1 * error * learningRate;
    }

    private float weightedSum(float[] inputs) {
        float sum = 0;
        for (int i = 0; i < inputs.length; i++) {
            sum += inputs[i] * weights[i];
        }
        sum += 1 * bias;
        return sum;
    }

    private float stepActivationFun(float sum) {
        if (sum >= 0) {
            return 1;
        } else {
            return 0;
        }
    }
}
