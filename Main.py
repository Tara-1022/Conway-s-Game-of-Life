from tkinter import *
from Game_of_Life import *

#preset board size
x, y = 10, 10

#called once the cells are selected
def start():
    for r in range(x):
        for c in range(y):
            if cells[r][c].get() == 1:
                selected_cells.add(Cell(r, c))
    show_evolution(selected_cells)

#called recursively to display the evolution; closes the window when 'quit' is clicked
def show_evolution(curr_cells):
    board = Grid(x, y, curr_cells)
    for widgets in window.winfo_children():
        widgets.destroy()
    for r in range(x):
        for c in range(y):
            if Cell(r, c) in board.alive_cells:
                b = Checkbutton(window, bg="yellow", onvalue=1, offvalue=0, indicatoron=False, width=3,
                            variable=cells[r][c])
            else:
                b = Checkbutton(window, bg="black", onvalue=1, offvalue=0, indicatoron=False, width=3,
                                variable=cells[r][c])
            b.grid(row=r + 1, column=c + 1)
            b.deselect()
    Button(window, text = "Next", fg = "gold", bg = "black", command = lambda: show_evolution(board.evolve())).grid(row = x+1,column = y+1)
    Button(window, text="Quit", fg="white", bg="red", command=lambda: window.destroy()).grid(
        row=x + 2, column=y + 1)

#initial set-up window
window = Tk()
window.title("Game of Life")
window.geometry('500x400')
#window.resizable(False, False)
cells = [[IntVar() for r in range(x)] for c in range(y)]
buttons = [[None]*y]*x
selected_cells = set()
for r in range(x):
    for c in range(y):
        b = Checkbutton(window, bg = "dark gray", onvalue=1, offvalue=0, indicatoron = False, width = 3, variable = cells[r][c])
        b.grid(row = r + 1, column = c + 1)
        buttons[r][c] = b

Label(window, text = "Select a cell to indicate it's alive.\n Click 'start' when done").grid(row = x+1, column = y + 1)
start = Button(window, text = "Start", fg = "gold", bg = "black", command = start)
start.grid(row = x+2, column = y + 1)

window.mainloop()
[urk21cs1022@code Game_of_Life]$ ^C
[urk21cs1022@code Game_of_Life]$ cat Game_of_Life.py 
#implementing Conway's Game of Life
from collections import namedtuple
Cell = namedtuple("Cell", ["row", "col"])

"""A class implementing a Game_of_Life grid"""
class Grid:
    offsets = [(-1,0), (1,0), (0,1), (0,-1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    def __init__(self, r, c, alive_cells = {}):
        self.alive_cells = alive_cells
        self.rows = r
        self.columns = c
    
    def evolve(self):
        next_alive = set(self.alive_cells)
        for row in range(self.rows):
            for col in range(self.columns):
                current_cell = Cell(row, col)
                alive = get_neighbours(self, current_cell)
                if current_cell in self.alive_cells:
                    if alive < 2 or alive > 3:
                        next_alive.remove(current_cell)
                else:
                    if alive == 3:
                        next_alive.add(current_cell)
        return next_alive

    def __str__(self):
        rep = ""
        for row in range(self.rows):
                rep += "".join("1 " if Cell(row, col) in self.alive_cells else "0 " for col in range(self.columns))
                rep += "\n"
        return rep

"""A function to get the number of alive neighbours of a cell"""
def get_neighbours(grid, cell):
        alive = 0
        for offset in grid.offsets:
                if Cell(cell.row + offset[0], cell.col + offset[1]) in grid.alive_cells:
                        alive += 1
        return alive
