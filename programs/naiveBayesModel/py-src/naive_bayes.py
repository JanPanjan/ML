import util
import column_table
import class_table


class Naive_bayes:
    def __init__(self):
        self.col_tables = []
        self.cls_table = None

    def train(self, feature_mat, response_vec):
        self.cls_table = class_table.ClassTable(response_vec)
        num_of_cols = len(feature_mat[0])

        for col_index in range(num_of_cols):
            col = util.extract_column(feature_mat, col_index)
            self.col_tables.append(column_table.ColumnTable(col, response_vec))

    def predict(self, vals_to_predict, response_vec):
        self.cls_table = class_table.ClassTable(response_vec)
        cls_vals = self.cls_table.get_cls_vals()
        most_prob_val = 0.0
        most_prob_cls = ""

        for cls_val in cls_vals:
            prob = 1

            for col in range(0, len(self.col_tables)):
                prob *= self.col_tables[col].get_probability(vals_to_predict[col], cls_val)

            prob *= self.cls_table.get_probability(cls_val)

            print(str(cls_val), " ", str(prob))
            if most_prob_val < prob:
                most_prob_val = prob
                most_prob_cls = cls_val

        return most_prob_cls

    def display(self):
        for table in self.col_tables:
            table.display()
