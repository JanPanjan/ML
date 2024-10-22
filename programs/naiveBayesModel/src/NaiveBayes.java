import java.lang.reflect.Array;
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

    public String predict(String[] valuesToPredict) {
        ArrayList<String> classValues = classTable.getClassValues();
        double mostProbableValue = Double.MIN_VALUE;    
        String mostProbableClass = "";

        for (String classValue : classValues) {
            double probability = 1;

            for (int colIndex = 0; colIndex < columnTables.length; colIndex++) {
                probability *= columnTables[colIndex].getProbability(valuesToPredict[colIndex], classValue);
            }

            probability *= classTable.getProbability(classValue);

            System.out.println(classValue + " " + probability);
            if (mostProbableValue < probability) {
                mostProbableValue = probability;
                mostProbableClass = classValue;
            }

        }
        return mostProbableClass;
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

    public double getProbability(String columnValue, String classValue) {
        int rowIndex = columnValues.indexOf(columnValue);
        int colIndex = classValues.indexOf(classValue);
        int count = counts[rowIndex][colIndex];
        int sum = 0;

        for (int row = 0; row < columnValues.size(); row++) {
            sum += counts[row][colIndex];
        }

        return (double)count / sum;
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

    public ArrayList<String> getClassValues() {
        return classValues;
    }

    public double getProbability(String classValue) {
        int index = classValues.indexOf(classValue);
        int count = counts[index];
        int sum = 0;

        for (int col = 0; col < classValues.size(); col++) {
            sum += counts[col];
        }

        return (double)count / sum;
    }
}
