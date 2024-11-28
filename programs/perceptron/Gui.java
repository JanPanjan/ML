import javax.swing.*;
import java.awt.*;

public class Gui extends JPanel {
	private int FRAME_WIDTH = 800;
	private int FRAME_HEIGTH = 800;
	private Drawable[] drawables;

	// ustvari nek Gui, ki bo kazal točke
	public Gui(Drawable[] drawables) {
		this.drawables = drawables;
		JFrame frame = new JFrame();
		frame.setSize(FRAME_WIDTH, FRAME_HEIGTH);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.add(this);
		frame.setVisible(true);
	}

	// Izriše stvari na ekran
	public void paint(Graphics g) {
		Graphics2D g2d = (Graphics2D) g;

		g2d.setColor(Color.WHITE);
		g2d.fillRect(0, 0, FRAME_WIDTH, FRAME_HEIGTH);

		for (Drawable d : drawables) {
			d.draw(g2d, FRAME_WIDTH, FRAME_HEIGTH);
		}
	}
}
