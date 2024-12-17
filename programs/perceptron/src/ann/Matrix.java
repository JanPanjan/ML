package perceptron.src.ann;

import java.util.function.Function;

public class Matrix {
    private final float[][] values;

    /**
     * Constructs a Matrix object from a two-dimensional array of floats.
     * Enforces consistent dimensionality.
     * @param values 2D array of floats representing the matrix values.
     */
    public Matrix(float[][] values) {
        if (values == null) {
            throw new IllegalArgumentException("Enter values to create a Matrix");
        }
        if (values.length == 0) {
            throw new IllegalArgumentException("At least one row needed");
        }
        if (values[0].length == 0) {
            throw new IllegalArgumentException("At least one column needed");
        }

        int rowLen = values[0].length;
        for (float[] row : values) {
            if (row.length != rowLen) {
                throw new IllegalArgumentException("Inconsistent row lengths");
            }
        }

        this.values = deepCopy(values);
    }
    public Matrix(float[] values1D) {
        float[][] values = {values1D};
        if (values == null) {
            throw new IllegalArgumentException("Enter values to create a Matrix");
        }
        if (values.length == 0) {
            throw new IllegalArgumentException("At least one row needed");
        }
        if (values[0].length == 0) {
            throw new IllegalArgumentException("At least one column needed");
        }

        int rowLen = values[0].length;
        for (float[] row : values) {
            if (row.length != rowLen) {
                throw new IllegalArgumentException("Inconsistent row lengths");
            }
        }

        this.values = deepCopy(values);
    }

    /**
     * Returns the number of columns in the matrix.
     * @return Number of columns.
     */
    public int getCols() {
        return values[0].length;
    }

    /**
     * Returns the number of rows in the matrix.
     * @return Number of rows.
     */
    public int getRows() {
        return values.length;
    }

    /**
     * Logs matrix dimensions and values to the console.
     */
    public void log() {
        System.out.println("Dimensions: (" + getRows() + " | " + getCols() + ")");
        for (float[] row : values) {
            for (float val : row) {
                System.out.printf("%.2f ", val);
            }
            System.out.println();
        }
    }

    /**
     * Returns a deep copy of the matrix values.
     * @return 2D array clone of the matrix values.
     */
    public float[][] getValues() {
        return deepCopy(values);
    }

    /**
     * Helper method to create a deep copy of a 2D array.
     */
    private static float[][] deepCopy(float[][] array) {
        float[][] copy = new float[array.length][];
        for (int i = 0; i < array.length; i++) {
            copy[i] = array[i].clone();
        }
        return copy;
    }

    /**
     * Creates a zero Matrix object of desired dimensions.
     * @param cols Number of columns.
     * @param rows Number of rows.
     * @return Matrix object filled with zeros.
     */
    public static Matrix zeroMatrix(int cols, int rows) {
        if (cols < 1) {
            throw new IllegalArgumentException("You need at least one column");
        }
        if (rows < 1) {
            throw new IllegalArgumentException("You need at least one row");
        }

        float[][] values = new float[rows][cols];
        return new Matrix(values);
    }

    /**
     * Creates a one Matrix object of desired dimensions.
     * @param cols Number of columns.
     * @param rows Number of rows.
     * @return Matrix object filled with ones.
     */
    public static Matrix oneMatrix(int cols, int rows) {
        if (cols < 1) {
            throw new IllegalArgumentException("You need at least one column");
        }
        if (rows < 1) {
            throw new IllegalArgumentException("You need at least one row");
        }

        float[][] values = new float[rows][cols];
        for (int i = 0 ; i < rows ; i++) {
            for (int j = 0 ; j < cols ; j++) {
                values[i][j] = 1.0f;
            }
        }
        return new Matrix(values);
    }

    /**
     * Creates a random Matrix object of desired dimensions.
     * All values are between -2 and 2.
     * @param cols Number of columns.
     * @param rows Number of rows.
     * @return Matrix object filled with random values.
     */
    public static Matrix randomMatrix(int cols, int rows) {
        if (cols < 1) {
            throw new IllegalArgumentException("You need at least one column");
        }
        if (rows < 1) {
            throw new IllegalArgumentException("You need at least one row");
        }

        float[][] values = new float[rows][cols];
        for (int i = 0 ; i < rows ; i++) {
            for (int j = 0 ; j < cols ; j++) {
                values[i][j] = (float) (Math.random() * 4 - 2); // Random values between -2 and 2
            }
        }
        return new Matrix(values);
    }

    /**
     * Adds a scalar to every element of the matrix.
     * @param scalar Value to be added.
     * @return A new Matrix after addition.
     */
    public Matrix addScalar(float scalar) {
        float[][] newValues = getValues();
        for (int i = 0 ; i < getRows() ; i++) {
            for (int j = 0 ; j < getCols() ; j++) {
                newValues[i][j] += scalar;
            }
        }
        return new Matrix(newValues);
    }

    /**
     * Applies a transformation function to each element of the matrix.
     * @param func Transformation function.
     * @return A new Matrix after applying the function.
     */
    public Matrix map(Function<Float, Float> func) {
        float[][] newValues = getValues();
        for (int i = 0 ; i < getRows() ; i++) {
            for (int j = 0 ; j < getCols() ; j++) {
                newValues[i][j] = func.apply(newValues[i][j]);
            }
        }
        return new Matrix(newValues);
    }

    /**
     * Multiplies two matrices.
     * @param m1 First operand.
     * @param m2 Second operand.
     * @return A new Matrix as the result of multiplication.
     */
    public static Matrix multiply(Matrix m1, Matrix m2) {
        if (m1.getCols() != m2.getRows()) {
            throw new IllegalArgumentException("Invalid dimensions for matrix multiplication");
        }
        int rows = m1.getRows();
        int cols = m2.getCols();
        int n = m1.getCols();
        float[][] result = new float[rows][cols];
        float[][] m1Values = m1.values;
        float[][] m2Values = m2.values;

        for (int row = 0 ; row < rows ; row++) {
            for (int col = 0 ; col < cols ; col++) {
                for (int offset = 0 ; offset < n ; offset++) {
                    result[row][col] += m1Values[row][offset] * m2Values[offset][col];
                }
            }
        }
        return new Matrix(result);
    }

    /**
     * Transposes the matrix.
     * @return A new Matrix that is the transpose.
     */
    public Matrix transpose() {
        int rows = getRows();
        int cols = getCols();
        float[][] transposedValues = new float[cols][rows];
        for (int i = 0; i < cols; i++) {
            for (int j = 0; j < rows; j++) {
                transposedValues[i][j] = values[j][i];
            }
        }
        return new Matrix(transposedValues);
    }

    /**
     * Adds two matrices element-wise.
     * @param mat1 First matrix.
     * @param mat2 Second matrix.
     * @return A new Matrix after addition.
     */
    public static Matrix addMatrices(Matrix mat1, Matrix mat2) {
        if (mat1.getRows() != mat2.getRows() || mat1.getCols() != mat2.getCols()) {
            throw new IllegalArgumentException("Matrices must have the same dimensions to be added.");
        }

        int rows = mat1.getRows();
        int cols = mat1.getCols();
        float[][] summedValues = new float[rows][cols];
        float[][] m1 = mat1.values;
        float[][] m2 = mat2.values;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                summedValues[i][j] = m1[i][j] + m2[i][j];
            }
        }
        return new Matrix(summedValues);
    }

    /**
     * Subtracts the second matrix from the first matrix element-wise.
     * @param mat1 First matrix.
     * @param mat2 Second matrix.
     * @return A new Matrix after subtraction.
     */
    public static Matrix subtractMatrices(Matrix mat1, Matrix mat2) {
        if (mat1.getRows() != mat2.getRows() || mat1.getCols() != mat2.getCols()) {
            throw new IllegalArgumentException("Matrices must have the same dimensions to be subtracted.");
        }

        int rows = mat1.getRows();
        int cols = mat1.getCols();
        float[][] subtractedValues = new float[rows][cols];
        float[][] m1 = mat1.values;
        float[][] m2 = mat2.values;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                subtractedValues[i][j] = m1[i][j] - m2[i][j];
            }
        }
        return new Matrix(subtractedValues);
    }

    /**
     * Multiplies two matrices element-wise.
     * @param mat1 First matrix.
     * @param mat2 Second matrix.
     * @return A new Matrix after element-wise multiplication.
     */
    public static Matrix multiplyByElement(Matrix mat1, Matrix mat2) {
        if (mat1.getRows() != mat2.getRows() || mat1.getCols() != mat2.getCols()) {
            throw new IllegalArgumentException("Matrices must have the same dimensions for element-wise multiplication.");
        }

        int rows = mat1.getRows();
        int cols = mat1.getCols();
        float[][] multipliedValues = new float[rows][cols];
        float[][] m1 = mat1.values;
        float[][] m2 = mat2.values;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                multipliedValues[i][j] = m1[i][j] * m2[i][j];
            }
        }
        return new Matrix(multipliedValues);
    }

    /**
     * Multiplies each element of the matrix by a scalar value.
     * @param scalar Scalar value to multiply.
     * @return A new Matrix after scalar multiplication.
     */
    public Matrix multiplyScalar(float scalar) {
        int rows = getRows();
        int cols = getCols();
        float[][] scaledValues = new float[rows][cols];
        float[][] vals = values;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                scaledValues[i][j] = vals[i][j] * scalar;
            }
        }
        return new Matrix(scaledValues);
    }
}