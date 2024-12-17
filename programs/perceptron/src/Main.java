package perceptron.src;

public class Main {
    static Point[] data = generateData(500);

    static Gui gui = new Gui(data);

    public static void main(String[] args) {
        Perceptron perceptron = new Perceptron(2,0.1f);

        for (Point p : data) {
            test(perceptron);

            float[] input = {p.x, p.y};
            float correct = p.label;

            perceptron.fitOne(input,correct);

            try {
                Thread.sleep(50);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        }
    }

    public static void test(Perceptron model) {
        for (Point p : data) {
            float[] input = {p.x, p.y};
            float prediction = model.predictOne(input);
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