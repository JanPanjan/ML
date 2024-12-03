import random as rand


class Point:
    def __init__(self) -> None:
        self.__x = rand.random();
        self.__y = rand.random();
    
        # točki doda label glede na njuni koordinati
        # y = kx je linearna funckija oz. premica, ko k = 1
        # x večji od y, pomeni, da je k > 1
        # 1: valid
        # 0: not valid
        if self.__x > self.__y:
            self.__label = 1
        else:
            self.__label = 0

        # model mora uganiti, katere točke so v redu in katere ne
        # na začetku ni uganil še nobedene točke
        self.__guessed = False

    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, val: float) -> None:
        self.__x = val
    
    @property
    def y(self) -> float:
        return self.__y
    
    @y.setter
    def y(self, val: float) -> None:
        self.__y = val

    @property
    def guessed(self) -> bool:
        return self.guessed
    
    @guessed.setter
    def guessed(self, val: bool) -> None:
        self.__guessed = val
    
    def draw(self, root, canvas, frame_width: int, frame_height: int) -> None:
        """
        Izriše točko na canvas in ji dodeli barvo in fill glede na 
        label in guess modela.
        """
        x = int(self.__x * frame_width)
        y = int(self.__x * frame_height)
        pw = 12

        # !!!
        # ali lahko naredim nek interface v pythonu, da passam samo te vrednosti, ki se
        # spreminjajo (pw, fill)? wrapper? can I? to bi bilo hudo.
        # !!!
        if self.__label == 1:
            canvas.create_oval(root, x-pw, y-pw, x+pw, y+pw, outline="black", fill="white", width=1) # width=12?
        else:
            canvas.create_oval(root, x-pw, y-pw, x+pw, y+pw, outline="black", fill="black", width=1) # width=12?
        
        pw = 6

        if self.__guessed:
            canvas.create_oval(root, x-pw, y-pw, x+pw, y+pw, outline="black", fill="green", width=1)
        else:
            canvas.create_oval(root, x-pw, y-pw, x+pw, y+pw, outline="black", fill="red", width=1)

