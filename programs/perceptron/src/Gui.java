package perceptron.src;

import javax.swing.*;
import java.awt.*;

public class Gui extends JPanel {
    private int FRAME_WIDTH = 800;
    private int FRAME_HEIGHT = 800;

    private Drawable[] drawables;

    public Gui(Drawable[] drawables) {
        this.drawables = drawables;

        JFrame frame = new JFrame();
        frame.setSize(FRAME_WIDTH, FRAME_HEIGHT);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.add(this);
        frame.setVisible(true);
    }

    public void setDrawable(Drawable drawable) {
        Drawable[] drw = {drawable};
        this.drawables = drw;
    }

    public void paint(Graphics g) {
        Graphics2D g2d = (Graphics2D) g;

        g2d.setColor(Color.WHITE);
        g2d.fillRect(0, 0, FRAME_WIDTH, FRAME_HEIGHT);
        for (Drawable d : drawables) {
            d.draw(g2d, FRAME_WIDTH, FRAME_HEIGHT);
        }
    }
}
