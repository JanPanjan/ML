from frequency_table import FrequencyTable
from display import Display
from numpy import array
import math


class DecisionTree:
    def __init__(self) -> None:
        self.display = Display(self)

    def train(self, X:list, Y:list, col_names:list) -> None:
        """ Train v sklopu decision tree razumem kot ustvari decision tree
        glede na information gain od podatkov. """
        f_mat = array(X).T
        c_vec = Y
        self.feature_col_names = col_names[:-1]
        self.ft = FrequencyTable(f_mat, self.feature_col_names, c_vec)

    def __entropy(self, probabilites: dict) -> float:
        """ calculates entropy for attribute value. calculated as:
        $info(T) = \sum_{j=1}^{n} -p_j log_2(p_j)$ (če vm to kej pove)
        p_j: relative frequency (probability) of class j in attribute T """
        entropy = 0

        for p in probabilites.values():
            if p != 0:
                entropy += (-p * math.log2(p))

        return entropy

    def __ibs(self) -> float:
        """ calculates information before split. calculated for class attribute.  """
        return self.__entropy(self.ft.cls_table)

    def __ias(self, attribute: str) -> float:
        """ calculates information after split. calculated for given feature attribute.  """
        info = 0
        n_rows = len(self.ft.c_vec)

        for val, cls_p in self.ft.fr_table[attribute].items():
            # e.g. attribute = "Outlook", val = "Sunny", p = {"Yes": ...}
            # val_count: "Sunny" znotraj "Outlook"
            # atr_p: probability od sunny
            # e: entropy for sunny's yes no distribution
            val_count = len(self.ft.val_id_table[attribute][val])
            atr_p = val_count / n_rows
            e = self.__entropy(cls_p)
            info += atr_p * e  # doda uteženo entropijo v result

        return info

    def __info_gain(self, attribute: str) -> float:
        """ calculates information gain. calculated from ibs and ias.  """
        return self.__ibs(attribute) - self.__ias(attribute)

    def __make_entropy_table(self):
        """ makes a table for an attribute with unique attribute values and
        their corresponding entropy in data.  """
        pass

    def __get_best_atr(self):
        pass

    def predict(self, case: list):
        """ predicts class value for a given case based on a decision tree. """
        pass