import util
import column_table
import class_table


class Naive_bayes:
    def __init__(self):
        self.col_tables  = []
        self.class_table = None

    def train(self, feature_mat, response_vec):
        self.class_table = ClassTable(response_vec)
        num_of_cols = len(feature_mat[0])

        for col_index in range(num_of_cols):
            col = util.extract_column(feature_mat, col_index)
            self.col_tables.append(ColumnTable(col, response_vec))

    # def predict(row):

    def display(self):
        for table in self.col_tables:
            table.display()


class ColumnTable:
    def __init__(self, feature_mat, response_vec):
        self.col_vals   = util.unique(feature_mat)
        self.class_vals = util.unique(response_vec)
        self.counts     = [[0] * len(self.class_vals) for _ in range(len(self.col_vals))]

        for row in range(0, len(feature_mat)):
            col_val   = feature_mat[row]
            class_val = response_vec[row]

            count_row = self.col_vals.index(col_val)
            count_col = self.class_vals.index(class_val)

            self.counts[count_row][count_col] += 1

    def display(self):
        for row in range(len(self.counts)):
            print(str(self.col_vals[row]), ": ", end = "")
            print(self.counts[row])


class ClassTable:
    def __init__(self, response_vec):
        self.class_vals = util.unique(response_vec)
        self.counts     = [0] * len(self.class_vals)

        for item in response_vec:
            class_index = self.class_vals.index(item)
            self.counts[class_index] += 1
