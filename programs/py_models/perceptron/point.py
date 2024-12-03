import random as rand


class Point:
    def __init__(self) -> None:
        """
        Vsaka točka ima neki x in y koordinati ter label, ki je
        določen glede na nek pogoj (v našem primeru linearna funkcija).
        y = kx je x, ko k = 1. x večji od y, pomeni, da je k > 1, zato
        1 = valid  in 0 = not valid.
        """
        self.__x = rand.random();
        self.__y = rand.random();
        self.__label = 1 if self.__x > self.__y else 0

        """ 
        Model mora uganiti, katere točke so v redu in katere ne
        na začetku ni uganil še nobedene točke, oziroma, prilagaja
        svoje parametre (error), dokler ne najde ravnovesja.
        """
        self.__guessed = False
    
    @property
    def x(self) -> float:
        return self.__x
    
    @property
    def y(self) -> float:
        return self.__y
    
    @property
    def label(self) -> int:
        return self.__label
    
    @label.setter
    def label(self, val:int) -> None:
        self.__label = val
    
    @property
    def guessed(self) -> bool:
        return self.__guessed
    
    @guessed.setter
    def guessed(self, val:bool) -> None:
        self.__guessed = val
    
    
    def draw(self, canvas, frame_width: int, frame_height: int) -> None:
        """
        Izriše točko na canvas in ji dodeli barvo in fill glede na 
        label in guess modela.
        """
        # scale coordinates to canvas size
        x = int(self.__x * frame_width)
        y = int(self.__y * frame_height)

        # set color based on label and whether it was guessed
        color = "red" if self.__label == 0 else "green"

        if not self.__guessed:
            color = "gray"

        # draw the point
        r = 4  # radius
        canvas.create_oval(x - r, y - r, x + r, y + r, fill=color)

        return