package perceptron.src;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class MnistLoader {
    public static final int PIXEL_COUNT = 28 * 28;

    /**
     * Loads MNIST digits from a CSV file.
     * @param csvPath the path to the CSV file
     * @return a list of MnistDigit objects
     * @throws IOException if the file can't be read
     */
    public List<MnistDigit> load(String csvPath) throws IOException {
        List<MnistDigit> digits = new ArrayList<>();

        try (BufferedReader br = new BufferedReader(new FileReader(csvPath))) {
            String line = br.readLine(); // read the header line

            while ((line = br.readLine()) != null) {
                // Split by comma
                String[] values = line.split(",");

                // The first value is the label
                int label = Integer.parseInt(values[0]);

                // The next 784 values are pixels
                float[] pixels = new float[PIXEL_COUNT];
                for (int i = 0; i < PIXEL_COUNT; i++) {
                    pixels[i] = Float.parseFloat(values[i + 1]);
                }

                MnistDigit digit = new MnistDigit(label, pixels);
                digits.add(digit);
            }
        }

        return digits;
    }
}
