import util


class ClassTable:
    def __init__(self, response_vec):
        self.class_vals = util.unique(response_vec)
        self.counts     = [0] * len(self.class_vals)

        for item in response_vec:
            class_index = self.class_vals.index(item)
            self.counts[class_index] += 1
