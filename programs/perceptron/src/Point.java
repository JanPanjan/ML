package perceptron.src;

import java.awt.*;
import java.util.Random;

public class Point implements Drawable{

    float x;
    float y;
    float label;
    boolean guessed;

    public Point() {
        Random r = new Random();
        x = r.nextFloat();
        y = r.nextFloat();

        if (x > y){
            label = 1;
        }else {
            label = 0;
        }
        guessed = false;
    }

    @Override
    public void draw(Graphics2D g2d, int frameWidth, int frameHeight) {
        int displayX = (int) (x * frameWidth);
        int displayY = (int) (y * frameHeight);

        g2d.setColor(Color.black);

        if (label == 1){
            g2d.drawOval(displayX, displayY, 12, 12);
        }else {
            g2d.fillOval(displayX, displayY, 12, 12);
        }

        g2d.setColor(Color.red);
        if (guessed){
            g2d.setColor(Color.green);
        }else {
            g2d.setColor(Color.red);
        }

        g2d.fillOval(displayX + 3, displayY + 3, 6, 6);
    }
}
