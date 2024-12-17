package perceptron.src;

import perceptron.src.ann.ArtificialNeuralNetwork;
import perceptron.src.ann.ActivationFunction;
import perceptron.src.ann.Layer;

import java.io.IOException;
import java.util.List;

public class Main3 {
    public static void main(String[] args) throws IOException, InterruptedException {
        MnistLoader loader = new MnistLoader();
        List<MnistDigit> digits = loader.load("programs/data/mnist_test.csv");
        System.out.println("Digits loaded: " + digits.size());

        ArtificialNeuralNetwork model = new ArtificialNeuralNetwork(784, .0001f, new Layer[]{
                new Layer(64, ActivationFunction.sigmoid),
                new Layer(32, ActivationFunction.sigmoid),
                new Layer(32, ActivationFunction.sigmoid),
                new Layer(10, ActivationFunction.sigmoid),
        });

        // Histogram display
        LearningTracker tracker = new LearningTracker();
        Gui trackerGui = new Gui(new Drawable[] {tracker});

        // Training loop
        int epoch = 1;
        int EPOCHS_TO_COMPLETE = 30;

        while (epoch < EPOCHS_TO_COMPLETE) {
            float epochLoss = 0;

            for (MnistDigit digit : digits) {
                float[] inputs = digit.getPixels();
                float[] targets = digit.getLabel();

                epochLoss += model.fitOne(inputs, targets);
            }

            tracker.submitEpoch(epochLoss);
            trackerGui.repaint();

            epoch++;
        }

        Gui gui = new Gui(new Drawable[]{});

        for (MnistDigit digit : digits) {
            float[] inputs = digit.getPixels();
            digit.guess = model.predictOne(inputs);
            gui.setDrawable(digit);
            gui.repaint();

            Thread.sleep(1500);
        }
    }
}
