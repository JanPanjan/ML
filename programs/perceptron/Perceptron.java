import java.util.Random;

// To je naš model, ki bo ugibal in se učil katere točke so prave.
public class Perceptron {
	private float[] weights;
	private float bias;
	private float learningRate;

	public Perceptron(int inputSize, float learningRate) {
		this.learningRate = learningRate;
		this.weights = new float[inputSize];
		Random rand = new Random();

		for (int i = 0; i < inputSize; i++) {
			this.weights[i] = rand.nextFloat(-1, 1);
		}
		this.bias = rand.nextFloat(-1, 1);
	}

	public float predictOne(float[] input) {
		float sum = weightedSum(input);
		return stepActivationFun(sum);
	}

	/**
	 * Funckija uči model, kaj so pravilne rešitve, tako da se weights an bias posodabljajo
	 * @param input
	 * @param correct
	 */
	public void fitOne(float[] input, float correct) {
		float guess = predictOne(input);
		float error = correct - guess;

		for (int i = 0; i < this.weights.length; i++) {
			this.weights[i] += input[i] * error * this.learningRate;
		}
		this.bias += 1 * error * this.learningRate;
	}

	public float weightedSum(float[] input) {
		float sum = 0;

		for (int i = 0; i < input.length; i++) {
			sum += input[i] * this.weights[i];
		}
		sum += 1 * this.bias;
		return sum;
	}

	public float stepActivationFun(float sum) {
		if (sum >= 0) {
			return 1;
		}
		return 0;
	}
}
