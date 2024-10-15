import java.util.ArrayList;
import java.util.Arrays;

class NaiveBayes {
    private ColumnTable[] columnTables;
    private ClassTable classTable;

    public void train(String[][] X, String[] Y) {
        int numOfCols = X[0].length;
        columnTables = new ColumnTable[numOfCols];

        for (int colIndex = 0; colIndex < numOfCols; colIndex++) {
            String[] column = Util.extractColumn(X, colIndex);
            columnTables[colIndex] = new ColumnTable(column, Y);
        }

        classTable = new ClassTable(Y);
    }

    public String predict(String[][] row) {
        return null;
    }

    public void display() {
        for (ColumnTable table : columnTables) {
            table.display();
        }
    }
}

class ColumnTable{
    private int[][] counts;
    private ArrayList<String> columnValues;
    private ArrayList<String> classValues;

    public ColumnTable(String[] column, String[] Y) {
        columnValues = Util.unique(column);
        classValues = Util.unique(Y);
        counts = new int[columnValues.size()][classValues.size()];

        for (int row = 0; row < column.length; row++) {
            String columnValue = column[row];
            String classValue = Y[row];
            int countRow = columnValues.indexOf(columnValue);
            int countColumn = classValues.indexOf(classValue);

            counts[countRow][countColumn]++;
        }
    }

    public void display() {
        for (int row = 0; row < counts.length; row++) {
            System.out.print(columnValues.get(row) + ": ");
            System.out.println(Arrays.toString(counts[row]));
        }
    }
}

class ClassTable{
    private int[] counts;
    private ArrayList<String> classValues;

    public ClassTable(String[] Y){
        classValues = Util.unique(Y);
        counts = new int[classValues.size()];

        for (String classValue : Y) {
            int classIndex = classValues.indexOf(classValue);
            counts[classIndex]++;
        }
    }
}