package perceptron.src;

import java.awt.*;
import java.util.ArrayList;
import java.util.List;

public class LearningTracker implements Drawable {
    private long startTime;
    private List<Float> losses = new ArrayList<>();
    private float bestLoss = Float.MAX_VALUE;

    public LearningTracker() {
        this.startTime = System.currentTimeMillis();
    }

    /**
     * Record a new epoch loss.
     * @param loss The loss value for this epoch.
     */
    public void submitEpoch(float loss) {
        losses.add(loss);
        if (loss < bestLoss) {
            bestLoss = loss;
        }
    }

    @Override
    public void draw(Graphics2D g2d, int frameWidth, int frameHeight) {
        g2d.setColor(Color.DARK_GRAY);
        g2d.fillRect(0, 0, frameWidth, frameHeight);

        if (losses.isEmpty()) {
            g2d.setColor(Color.RED);
            g2d.drawString("No epochs recorded yet.", 10, 20);
            return;
        }

        long currentTime = System.currentTimeMillis();
        float elapsedSeconds = (currentTime - startTime) / 1000f;

        float maxLoss = 0;
        for (float loss : losses) {
            if (loss > maxLoss) {
                maxLoss = loss;
            }
        }
        if (maxLoss == 0) {
            maxLoss = 1;
        }

        int margin = 40;
        int numEpochs = losses.size();
        int chartWidth = frameWidth - 2 * margin;
        int chartHeight = frameHeight - 2 * margin;

        int barWidth = Math.max(5, chartWidth / Math.max(numEpochs, 1));

        for (int i = 0; i < numEpochs; i++) {
            float loss = losses.get(i);
            float normalizedHeight = (loss / maxLoss) * chartHeight;
            int barX = margin + i * barWidth;
            int barY = frameHeight - margin - Math.round(normalizedHeight);

            g2d.setColor(Color.LIGHT_GRAY);
            g2d.fillRect(barX, barY, barWidth - 2, Math.round(normalizedHeight));

            if (barWidth > 20) {
                g2d.setColor(Color.BLACK);
                g2d.drawString(String.valueOf(i+1), barX + 2, frameHeight - margin + 15);
            }
        }

        // stats
        float lastLoss = losses.get(losses.size() - 1);
        float firstLoss = losses.get(0);
        float avgEpochTime = elapsedSeconds / numEpochs;

        g2d.setColor(Color.CYAN);
        FontMetrics fm = g2d.getFontMetrics();
        int lineHeight = fm.getHeight();
        int textX = frameWidth - margin - 150;
        int textY = margin;

        g2d.drawString(String.format("Time: %.1fs", elapsedSeconds), textX, textY);
        g2d.drawString(String.format("Avg Epoch Time: %.2fs", avgEpochTime), textX, textY + lineHeight);

        g2d.drawString(String.format("First: %.4f", firstLoss), textX, textY + 3 * lineHeight);
        g2d.drawString(String.format("Last: %.4f", lastLoss), textX, textY + 4 * lineHeight);
        g2d.drawString(String.format("Best: %.4f", bestLoss), textX, textY + 5 * lineHeight);

        g2d.drawString("Loss per Epoch (Current epoch: " + losses.size() + ")", margin, margin - 10);
    }
}
