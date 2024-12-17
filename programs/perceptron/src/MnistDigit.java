package perceptron.src;

import java.awt.*;
import java.awt.image.BufferedImage;

public class MnistDigit implements Drawable {
    private static final int WIDTH = 28;
    private static final int HEIGHT = 28;

    private int label;
    private float[] pixels;
    public float[] guess;

    /**
     * Constructs a MnistDigit from a label and pixel array.
     *
     * @param label The digit label (0-9)
     * @param pixels An array of length 784 (28x28), with values 0-255 representing grayscale intensity.
     */
    public MnistDigit(int label, float[] pixels) {
        if (pixels.length != WIDTH * HEIGHT) {
            throw new IllegalArgumentException("Pixels array must have length " + (WIDTH * HEIGHT));
        }
        this.label = label;
        this.pixels = pixels;
    }

    public float[] getLabel() {
        float[] labels = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
        labels[label] = 1;
        return labels;
    }

    public float[] getPixels() {
        return pixels;
    }

    @Override
    public void draw(Graphics2D g2d, int frameWidth, int frameHeight) {
        BufferedImage image = new BufferedImage(WIDTH, HEIGHT, BufferedImage.TYPE_BYTE_GRAY);

        // fill the BufferedImage with pixel data
        for (int y = 0; y < HEIGHT; y++) {
            for (int x = 0; x < WIDTH; x++) {
                int idx = y * WIDTH + x;
                int value = Math.round(pixels[idx]);
                int rgb = (value << 16) | (value << 8) | value;
                image.setRGB(x, y, rgb);
            }
        }

        float scaleX = frameWidth / (float) WIDTH;
        float scaleY = frameHeight / (float) HEIGHT;
        float scale = Math.min(scaleX, scaleY); // Keep aspect ratio

        int drawWidth = Math.round(WIDTH * scale);
        int drawHeight = Math.round(HEIGHT * scale);

        int xOffset = (frameWidth - drawWidth) / 2;
        int yOffset = (frameHeight - drawHeight) / 2;

        g2d.drawImage(image, xOffset, yOffset, drawWidth, drawHeight, null);

        g2d.setColor(Color.RED);
        g2d.drawString("Label: " + label, 50, 50);

        if (guess != null) {
            float max = 0;
            for (float digitGuess : guess) {
                if (digitGuess > max) {
                    max = digitGuess;
                }
            }
            for (int i = 0 ; i < 10 ; i++) {
                String pred = "-> " + i + ": " + guess[i];
                if (guess[i] == max) {
                    g2d.setColor(Color.GREEN);
                } else {
                    g2d.setColor(Color.RED);
                }

                g2d.drawString(pred, 50, 70 + (i * 15));
            }
        }
    }
}
