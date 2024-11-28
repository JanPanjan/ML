import java.awt.*;
import java.util.Random;

public class Point implements Drawable {
	private float x;
	private float y;
	private float label;
	private boolean guessed;

	// Ustvari točko z naključno x in y koordinato.
	// Če je x večji kot y, pomeni, da je točka valid (1),
	// drugače ni valid (0).
	public Point() {
		Random rand = new Random();
		x = rand.nextFloat();
		y = rand.nextFloat();

		if (x > y) {
			label = 1;
		} else {
			label = 0;
		}

		// vsaka točka je na začetku neoznačena oz. je model
		// še ni določil kot pravo točko al nekaj
		guessed = false;
	}

	public float getX() {
		return this.x;
	}

	public float getY() {
		return this.y;
	}

	public float getLabel() {
		return this.label;
	}

	public boolean getGuessed() {
		return this.guessed;
	}

	public void setGuessed(boolean guess) {
		this.guessed = guess;
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
