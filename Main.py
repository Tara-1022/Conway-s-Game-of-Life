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
