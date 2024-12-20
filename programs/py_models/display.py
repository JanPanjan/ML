class Display:
    def __init__(self, nb) -> None:
        self.nb = nb

    def hello(self):
        print("hello from display class!")

    def table(self):
        print("\n")
        print("Table: frekvence")
        print("================")
        for atr in self.nb.ft.table.items():
            spaces = "-" * (11 - len(atr[0]))
            print(atr[0], f"{spaces}-----------------------")
            for uq_val in self.nb.ft.table[atr[0]].items():
                print(f"  ", f"{uq_val[0]}:", " " * (8 - len(uq_val[0]))  , f"{uq_val[1]}")

    def fr_table(self):
        print("\n")
        print("Table: verjetja")
        print("================")
        for atr in self.nb.ft.fr_table.items():
            spaces = "-" * (11 - len(atr[0]))
            print(atr[0], f"{spaces}-----------------------")
            for uq_val in self.nb.ft.fr_table[atr[0]].items():
                print(f"  ", f"{uq_val[0]}:", " " * (8 - len(uq_val[0])), uq_val[1])

    def probabilities(self, probabilities):
        print("\nProbabilites:")
        print("=============")
        for val, prob in probabilities.items():
            spc = " " * (3 - len(val))
            print(val, spc, "{:.4f}".format(prob))

    def prediction(self, probabilities):
        if probabilities["Yes"] > probabilities["No"]:
            val = "Yes"
        else:
            val = "No"

        print(f"\nMost probable class: {val}")
        diff = abs((probabilities["Yes"] - probabilities["No"]))
        print("Difference: {:.4f}".format(diff))