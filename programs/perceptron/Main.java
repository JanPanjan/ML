public class Main {
	static Point[] data = generateData(500);
	static Gui gui = new Gui(data);

	public static void main(String[] args) {
		Perceptron pcp = new Perceptron(2, 0.5f);

		for (Point p : data) {
			test(pcp);

			float[] input = { p.getX(), p.getY() };
			float correct = p.getLabel();

			pcp.fitOne(input, correct);

			try {
				Thread.sleep(50);
			} catch (InterruptedException e) {
				throw new RuntimeException(e);
			}
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

	public static void test(Perceptron model) {
		for (Point p : data) {
			float[] input = { p.getX(), p.getY() };
			float prediction = model.predictOne(input);

			p.setGuessed(prediction == p.getLabel());
		}
		gui.repaint();
	}
}
