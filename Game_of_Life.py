#implementing base classes for Conway's Game of Life
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
