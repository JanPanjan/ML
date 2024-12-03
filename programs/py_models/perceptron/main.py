import point as p
from gui import Gui
from perceptron import Perceptron
import time

def generate_data(num_of_pts: int) -> list:
    """
    Funckija generira neko število točk in vrne seznam iz njih
    """
    return [p.Point() for _ in range(num_of_pts)]

def test(gui, pcp, data) -> None:
    """
    Funkcija naredi prediction na neki točki in posodobi njen
    label in guessed variables.
    """
    for p in data:
        input = [p.x, p.y]
        prediction = pcp.predict_one(input)
        p.guessed = (prediction == p.label)
    
    gui.paint()
    return

def update(gui, pcp, data, i=0) -> None:
    """
    Funkcija scheadula events t časa narazen. Te events se dajo na nek
    stack/queue (idfk) in jih mainloop izvede, ko je poklican. Funkcija
    se kliče, dokler ni šla čez vse točke.
    """
    if i < len(data):
        p = data[i]
        test(gui=gui, pcp=pcp, data=data)
        input = [p.x, p.y]
        correct = p.label
        pcp.fit_one(input, correct)
        gui.root.after(50, update, gui, pcp, data, i+1)

    return

def main() -> None:
    data = generate_data(1000)
    gui = Gui(data)
    pcp = Perceptron(2, 0.5)

    update(gui=gui, pcp=pcp, data=data)
    gui.root.mainloop()

    return

if __name__ == '__main__':
    main()