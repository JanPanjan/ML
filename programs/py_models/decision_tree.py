from frequency_table import FrequencyTable
from display import Display
from numpy import array
import math


class Node:
    def __init__(self, val: str) -> None:
        self.__key = val
        self.__next = {}
        self.__is_leaf = False

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, val:str) -> None:
        self.__key = val

    @property
    def next(self) -> dict:
        return self.__next

    @next.setter
    def next(self, child:dict) -> None:
        self.__next = child

    @property
    def is_leaf(self) -> bool:
        return self.__is_leaf

    @is_leaf.setter
    def is_leaf(self, val:bool) -> None:
        self.__is_leaf = val


class DecisionTree:
    def __init__(self) -> None:
        self.display = Display(self)


    def train(self, X:list, Y:list, col_names:list) -> None:
        """ Train v sklopu decision tree razumem kot ustvari decision tree
        glede na information gain od podatkov. """
        f_mat = array(X).T
        c_vec = Y
        # odstrani class col name
        self.feature_col_names = col_names[:-1]
        # dobi frekvence
        self.ft = FrequencyTable(f_mat, self.feature_col_names, c_vec)
        # naredi tabelo infogain atributov
        self.__make_info_table()
        # izgradi drevo
        self.root = self.__build_tree(X, Y, self.feature_col_names)


    def predict(self, case: list):
        """ 
        Predicts class value for a given case by traversing the tree. 
        e.g. case ["Sunny", "Hot", "Normal", "False"] returns "Yes" or "No"
        """
        # start at root and continue downwards until we find a leaf
        cur = self.root
        while not cur.is_leaf:
            # get current node's attribute (key)
            atr = cur.key

            # find index of this attribute in feature names
            atr_id = self.feature_col_names.index(atr)

            # get case's value for this attribute
            # our tree's root has this value in its key
            val = case[atr_id]

            # move to next node based on this value
            if val in cur.next:
                cur = cur.next[val]
            # handle unseen values
            else:
                return self.__get_majority_class()


    def __build_tree(self, X:list, Y:list, feature_names:list) -> Node:
        """ 
        Function will build a decision tree recursively. 
        It returns the root of tree. 
        """
        # ----------------------- base case 1: ---------------------------
        # if all examples have same class (purity), make a leaf node with
        # class value
        if len(set(Y)) == 1:
            leaf = Node(Y[0])
            leaf.is_leaf = True
            return leaf
        
        # ----------------------- base case 2: -----------------------------
        # if Y is not pure and we used all of the features, we need to stop
        # recursion somehow - handling imperfect separation with a "best guess"
        if not feature_names:
            majority_class = self.__get_majority_class(Y)
            leaf = Node(majority_class)
            leaf.is_leaf = True
            return leaf

        # ----------------------- build tree ------------------------------
        # find best attribute to split the tree on
        best_atr = self.__get_best_atr()
        root = Node(best_atr)

        # for each unique values of best attribute, get subsets of examples with this value
        for val in self.ft.uq_val_table[best_atr]:
            # indexes of value to access elements of X and Y with val
            # first get all indexes, then take only the rows from subset
            all_ids = self.ft.val_id_table[val]
            cur_ids = [i for i, og_id in enumerate()]

            sub_X = [X[i] for i in ids]     # get rows from X (2D list)
            sub_Y = [Y[i] for i in ids]     # get elements from Y (1D list)

            # remove current attribute from feature names (for recursion)
            sub_features = [f for f in feature_names if f is not best_atr]
            # recursively build the tree
            root.next[val] = self.__build_tree(sub_X, sub_Y, sub_features)
        
        return root

    def __get_majority_class(Y:list) -> str:
        """ 
        For each value in set(Y), Y.count is called. 
        Returns most frequent class value.
        """
        return max(set(Y), key=Y.count)


    def __get_best_atr(self) -> str:
        """ returns the attribute with the biggest information gain. """
        return max(self.info_table, key=self.info_table.get)
        

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
            #     val_count: "Sunny" znotraj "Outlook"
            #     atr_p: probability od sunny
            #     e: entropy for sunny's yes no distribution
            val_count = len(self.ft.val_id_table[val])
            atr_p = val_count / n_rows
            e = self.__entropy(cls_p)

            # adds weighted entropy to result
            info += atr_p * e        

        return info


    def __info_gain(self, attribute: str) -> float:
        """ calculates information gain. calculated from ibs and ias. """
        return self.__ibs() - self.__ias(attribute)


    def __make_info_table(self):
        """ makes a table that holds attribute information gain. """
        self.info_table = {atr: self.__info_gain(atr) for atr in self.feature_col_names}
        return

