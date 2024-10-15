import java.util.ArrayList;

class Util {
    public static String[][] removeColumn(String[][] data, int colToRemove) {
        int numOfRows = data.length;
        int numOfCols = data[0].length - 1;
        String[][] newData = new String[numOfRows][numOfCols];

        for (int row = 0; row < numOfRows; row++) {
            ArrayList<String> newRow = new ArrayList<>();
            for (int col = 0; col < numOfCols; col++) {
                if (col != colToRemove) {
                    newRow.add(data[row][col]);
                }
            }
            String[] newRowArray = newRow.toArray(new String[0]);
            newData[row] = newRowArray;
        }

        return newData;
    }

    public static String[] extractColumn(String[][] data, int colToExtract) {
        String[] column = new String[data.length];
        for (int row = 0; row < data.length; row++) {
            column[row] = data[row][colToExtract];
        }
        return column;
    }

    public static ArrayList<String> unique(String[] columns) {
        ArrayList<String> uniqueValues = new ArrayList<>();
        for (String value : columns) {
            if (!uniqueValues.contains(value)) {
                uniqueValues.add(value);
            }
        }
        return uniqueValues;
    }
}