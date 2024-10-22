import util


class ColumnTable:
    def __init__(self, feature_mat, response_vec):
        self.col_vals = util.unique(feature_mat)
        self.cls_vals = util.unique(response_vec)
        self.counts = [[0] * len(self.cls_vals) for _ in range(len(self.col_vals))]

        for row in range(0, len(feature_mat)):
            col_val = feature_mat[row]
            class_val = response_vec[row]

            count_row = self.col_vals.index(col_val)
            count_col = self.cls_vals.index(class_val)

            self.counts[count_row][count_col] += 1

    def display(self):
        for row in range(len(self.counts)):
            print(str(self.col_vals[row]), ": ", end="")
            print(self.counts[row])

    def get_probability(self, col_val, cls_val):
        row_index = self.col_vals.index(col_val)
        col_index = self.cls_vals.index(cls_val)

        count = self.counts[row_index][col_index]
        sum = 0

        for row in range(0, len(self.col_vals)):
            sum += self.counts[row][col_index]

        return count / sum
