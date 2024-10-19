import util
import column_table
import class_table


class Naive_bayes:
    def __init__(self):
        self.col_tables  = []
        self.class_table = None

    def train(self, feature_mat, response_vec):
        self.class_table = class_table.ClassTable(response_vec)
        num_of_cols = len(feature_mat[0])

        for col_index in range(num_of_cols):
            col = util.extract_column(feature_mat, col_index)
            self.col_tables.append(column_table.ColumnTable(col, response_vec))

    # def predict(row):

    def display(self):
        for table in self.col_tables:
            table.display()
