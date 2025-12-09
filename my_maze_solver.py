from typing import Any
from random import random


class Cell:
    def __init__(self, row: int, col: int) -> None:
        self.row: int = row
        self.col: int = col
        self.prev: Cell | None = None

    def __add__(self, cell: "Cell") -> "Cell":
        return Cell(self.row + cell.row, self.col + cell.col)

    def __eq__(self, cell: "Cell") -> bool:
        return self.row == cell.row and self.col == cell.col

    def __str__(self) -> str:
        return f'{self.prev} ({self.row}, {self.col})'

    def __repr__(self) -> str:
        return f'Cell({self.row}, {self.col})'


class Maze:
    def __init__(self, size: int, start: Cell, end: Cell) -> None:
        chance_of_wall: float = 0.25
        self.start: Cell = start
        self.end: Cell = end
        self.__directions: list[Cell] = [Cell(1, 0), Cell(0, 1), Cell(-1, 0), Cell(0, -1)]
        self.__maze: list[list[Any]] = []
        for value in range(0, size * size):
            if value % size == 0:
                self.__maze.append([])
            entry = 0 if random() >= chance_of_wall else 1
            self.__maze[-1].append(entry)


    def is_wall(self, cell: Cell):
        return self.__maze[cell.row][cell.col] != 0


    def is_valid(self, cell: Cell):
        return 0 <= cell.row < len(self.__maze) and 0 <= cell.col < len(self.__maze[0])


    def set_visited(self, cell: Cell) -> None:
        self.__maze[cell.row][cell.col] = 'x'


    def get_valid_neighbors(self, cell: Cell) -> list[Cell]:
        neighbors: list[Cell] = []

        for direction in self.__directions:
            neighbor = cell + direction # __add__
            if self.is_valid(neighbor) and not self.is_wall(neighbor):
                neighbor.prev = cell
                neighbors.append(neighbor)

        return neighbors


    def __find_path_recursive(self, cells) -> Cell | None:
        neighbors: list[Cell] = []

        for cell in cells:
            self.set_visited(cell)
            if cell == self.end:
                return cell
            neighbors.extend(self.get_valid_neighbors(cell))

            # return self.__find_path_recursive(neighbors)

        if len(neighbors) == 0:
            return None

        return self.__find_path_recursive(neighbors)


    def find_path(self):
        if self.start == self.end:
            return self.start
        if self.is_wall(self.start) or self.is_wall(self.end):
            return None

        neighbors = self.get_valid_neighbors(self.start)
        return self.__find_path_recursive(neighbors)

    def trace_path(self, cell):
        path = []
        while cell is not None:
            path.append(cell)
            cell = cell.prev
        
        path = list(reversed(path))

        def get_direction(cell1, cell2):
            if cell1.row == cell2.row:
                return 'Right' if cell2.col > cell1.col else 'Left'
            else:
                return 'Down' if cell2.row > cell1.row else 'Up'
            
        for step in range(1, len(path) - 1):
            prev_cell = path[step - 1]
            curr_cell = path[step]
            next_cell = path[step + 1]

            path_dir1 = get_direction(prev_cell, curr_cell)
            path_dir2 = get_direction(curr_cell, next_cell)
            
            if path_dir1 in ('Left', 'Right') and path_dir2 in ('Left', 'Right'):
                self.__maze[curr_cell.row][curr_cell.col] = '→'
            elif path_dir1 in ('Up', 'Down') and path_dir2 in ('Up', 'Down'):
                self.__maze[curr_cell.row][curr_cell.col] = '↓'
            else:
                turn = {
                    ('Up', 'Right'): '↱',
                    ('Left', 'Down'): '⬐',
                    ('Up', 'Left'): '↰',
                    ('Right', 'Down'): '↴',
                    ('Down', 'Right'): '↳',
                    ('Left', 'Up'): '⬑',
                    ('Down', 'Left'): '↲',
                    ('Right', 'Up'): '⬏',
                }
                self.__maze[curr_cell.row][curr_cell.col] = turn[(path_dir1, path_dir2)]

        start = path[0]
        end = path[-1]
        self.__maze[start.row][start.col] = 'S'
        self.__maze[end.row][end.col] = 'E'



    def __str__(self) -> str:
        output = ''
        for row in self.__maze:
            output = '\n'.join([output, ' '.join([str(item) for item in row])])
        return output


def main():
    size: int = 20
    start = Cell(0, 0)
    end = Cell(size - 1, size - 1)
    

    print("Start = ", start)
    print("End = ", end)
    maze = Maze(size, start, end)
    print(maze)

    result = maze.find_path()
    print("\nShortest path from start to end:", result)

    if result is not None:
        maze.trace_path(result)
        print(maze)

    

if __name__ == '__main__':
    main()
