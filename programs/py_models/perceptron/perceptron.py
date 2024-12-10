import random as rand

class Perceptron:
    def __init__(self, input_size, learning_rate) -> None:
        self.__bias = rand.uniform(-1, 1)
        self.__weights = [rand.uniform(-1, 1) for _ in range(input_size)]
        self.__learning_rate = learning_rate

    def fit_one(self, input: list, correct: float) -> None:
        """
        S to funkcijo se model uči glede na dotedanje izračune, tako da
        sproti posodablja weights in bias, dokler ne najde nekega ravnovesja 
        med podatki.
        """
        guess = self.predict_one(input)
        error = correct - guess

        for i in range(len(self.__weights)):
            self.__weights[i] += input[i] * error * self.__learning_rate
        
        self.__bias += 1 * error * self.__learning_rate
        return
    
    def predict_one(self, input: list) -> float:
        """
        Predicta ali je point v redu ali ne glede na activation function.
        """
        sum = self.weighted_sum(input)
        return self.activation_fun(sum)

    def weighted_sum(self, input: list) -> float:
        """
        Izvede (tehtano) vsoto podatkov, tako da vsako vrednost množi z njenim
        corresponding weight in vse sešteje med sabo ter množi z biasom.
        """
        sum = 0

        for i in range(len(input)):
            sum += input[i] * self.__weights[i]

        sum += 1 * self.__bias
        return sum

    def activation_fun(self, sum: float) -> float:
        """
        To je logika našega modela. Glede na to funkcijo klasificira podane
        podatke. Uporabljena je preprosta sign funkcija, ki vrne 1, če je
        vsota večja ali enaka 1, sicer 0.
        """
        if sum >= 0:
            return 1
        else:
            return 0
