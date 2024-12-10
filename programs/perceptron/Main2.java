import ANN.ActivationFunction;
import ANN.ArtificialNeuralNetwork;
import ANN.Layer;

public class Main2 {
	static Point[] data = generateData(500);
	static Gui gui = new Gui(data);

	public static void main(String[] args) {
        // 2 inputa, 0.1f learning rate, 3 layers array
        ArtificialNeuralNetwork ann = new ArtificialNeuralNetwork(2, 0.1f, new Layer[] {
            // št nevronov v layerju, activation function
            new Layer(5, ActivationFunction.sigmoid),
            new Layer(5, ActivationFunction.sigmoid),
            new Layer(1, ActivationFunction.sigmoid)
        });

		for (Point p : data) {
			predictPoints(ann);

			float[] inputs = { p.getX(), p.getY() };
			float[] targets = { p.getLabel() };

			ann.fitOne(inputs, targets);
		}
	}

	// Metoda ustvari #numOfPts točk. To je to.
	public static Point[] generateData(int numOfPts) {
		Point[] pts = new Point[numOfPts];

		for (int i = 0; i < numOfPts; i++) {
			pts[i] = new Point();
		}

		return pts;
	}

	public static void predictPoints(ArtificialNeuralNetwork model) {
		for (Point p : data) {
			float[] input = { p.getX(), p.getY() };
            // baje vrne array samo z eno številko
			float prediction = Math.round(model.predictOne(input)[0]);

			p.setGuessed(prediction == p.getLabel());
		}
		gui.repaint();
	}
}
