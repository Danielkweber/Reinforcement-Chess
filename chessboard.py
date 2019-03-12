from tkinter import Tk, Label, Button, Canvas
import itertools

class Chessboard():
    def __init__(self, master, row = 8, col = 8, size = 200, color1 = "sky blue", color2 = "dodger blue",
        square_size = 85, border_top = 25, border_side = 45):

        master.title("Chess engine")
        colors = (color1, color2)
        color = itertools.cycle(colors)
        board = Canvas(master, bg = 'dark green', width=row*size, height=col*size)
        for row in range(row):
            for column in range(col):
                board.create_rectangle(border_side + square_size * row, border_top + square_size * column,
                    border_side + square_size * (row + 1), border_top + square_size * (column + 1),
                    fill = next(color), outline = "white")

                if column == col - 1:
                    next(color)    
        board.pack()


root = Tk()
my_gui = Chessboard(root)
root.mainloop()
