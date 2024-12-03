import tkinter as tk


class Gui:
    def __init__(self, drawables) -> None:
        self.__drawables = drawables
        self.__FRAME_WIDTH = 800
        self.__FRAME_HEIGHT = 800

        # ustvari main window frame
        self.root = tk.Tk()
        self.root.geometry(f"{self.__FRAME_WIDTH}x{self.__FRAME_HEIGHT}")

    def paint(self) -> None:
        """
        Ustvari in prikaže display zapolnjen z drawable objekti.
        """
        self.c = tk.Canvas(self.root, height=self.__FRAME_HEIGHT, width=self.__FRAME_WIDTH, bg="white")

        for d in self.__drawables:
            d.draw(self.root, self.c, self.__FRAME_WIDTH, self.__FRAME_HEIGHT)
