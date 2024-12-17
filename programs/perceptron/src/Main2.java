package perceptron.src;

import perceptron.src.ann.ActivationFunction;
import perceptron.src.ann.ArtificialNeuralNetwork;
import perceptron.src.ann.Layer;

public class Main2 {
    static Point[] data = generateData(500);

    static Gui gui = new Gui(data);

    public static void main(String[] args) {
        ArtificialNeuralNetwork ann = new ArtificialNeuralNetwork(2, 0.1f, new Layer[] {
                new Layer(5, ActivationFunction.sigmoid),
                new Layer(5, ActivationFunction.sigmoid),
                new Layer(1, ActivationFunction.sigmoid)
        });

        for (Point p : data) {
            test(ann);

            float[] inputs = {p.x, p.y};
            float[] targets = {p.label};

            ann.fitOne(inputs, targets);
        }


    }

    public static void test(ArtificialNeuralNetwork model) {
        for (Point p : data) {
            float[] input = {p.x, p.y};
            float prediction = Math.round(model.predictOne(input)[0]);

            p.guessed = (prediction == p.label);
        }
        gui.repaint();
    }

    public static Point[] generateData(int numOfPoints) {
        Point[] points = new Point[numOfPoints];
        for (int i = 0; i < numOfPoints; i++) {
            points[i] = new Point();
        }
        return points;
    }
}
