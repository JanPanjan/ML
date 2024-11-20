public class Main {
    public static void main(String[] args) {
        String[][] data = {
                { "Sunny", "Hot", "High", "False", "No" },
                { "Sunny", "Hot", "High", "True", "No" },
                { "Overcast", "Hot", "High", "False", "Yes" },
                { "Rainy", "Mild", "High", "False", "Yes" },
                { "Rainy", "Cool", "Normal", "False", "Yes" },
                { "Rainy", "Cool", "Normal", "True", "No" },
                { "Overcast", "Cool", "Normal", "True", "Yes" },
                { "Sunny", "Mild", "High", "False", "No" },
                { "Sunny", "Cool", "Normal", "False", "Yes" },
                { "Rainy", "Mild", "Normal", "False", "Yes" },
                { "Sunny", "Mild", "Normal", "True", "Yes" },
                { "Overcast", "Mild", "High", "True", "Yes" },
                { "Overcast", "Hot", "Normal", "False", "Yes" },
                { "Rainy", "Mild", "High", "True", "No" }
        };

        String[][] X = Util.removeColumn(data, 4);
        String[] Y = Util.extractColumn(data, 4);

        NaiveBayes nb = new NaiveBayes();
        nb.train(X, Y);
        nb.display();

        String[] toPredict = { "Sunny", "Hot", "High", "False" };
        String prediction = nb.predict(toPredict);
        System.out.println("Predicted:" + prediction);
    }
}
