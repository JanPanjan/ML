import tkinter as tk


class Gui:
    def __init__(self, drawables) -> None:
        self.__drawables = drawables
        self.__FRAME_WIDTH = 800
        self.__FRAME_HEIGHT = 800

        # ustvari main window frame
        self.root = tk.Tk()
        self.root.geometry(f"{self.__FRAME_WIDTH}x{self.__FRAME_HEIGHT}")

        # ustvari canvas
        self.c = tk.Canvas(height=self.__FRAME_HEIGHT, width=self.__FRAME_WIDTH, bg="white")
        self.c.pack()

        return

    def paint(self) -> None:
        """
        Ustvari in prikaže display zapolnjen z drawable objekti.
        """
        for d in self.__drawables:
            d.draw(self.c, self.__FRAME_WIDTH, self.__FRAME_HEIGHT)

        return
