import util


class ClassTable:
    def __init__(self, response_vec):
        self.cls_vals = util.unique(response_vec)
        self.counts     = [0] * len(self.cls_vals)

        for item in response_vec:
            class_index = self.cls_vals.index(item)
            self.counts[class_index] += 1

    def get_cls_vals(self):
        return self.cls_vals

    def get_probability(self, cls_val):
        index = self.cls_vals.index(cls_val)
        count = self.counts[index]
        sum = 0

        for col in range(0, len(self.cls_vals)):
            sum += self.counts[col]

        return (count / sum)
