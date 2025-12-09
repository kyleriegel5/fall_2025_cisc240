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


class Shape:
    def __init__(self, size: int) -> None:
        self.__directions: list[Cell] = [Cell(1, 0), Cell(0, 1), Cell(-1, 0), Cell(0, -1)]
        self.__shape: list[list[Any]] = []
        for value in range(0, size * size):
            if value % size == 0:
                self.__shape.append([])
            self.__shape[-1].append(0)

    def is_valid(self, cell: Cell):
        return 0 <= cell.row < len(self.__shape) and 0 <= cell.col < len(self.__shape[0])
    
    def get_plus(self, size):
        if size < 3 or size % 2 != 1:
            return None
        
        shape_len = len(self.__shape)
        center_cell = Cell(shape_len // 2, shape_len // 2)
        

        # Draw center
        self.__shape[center_cell.row][center_cell.col] = '+'

        # Draw 4 directions
        for direction in self.__directions:
            curr_cell = center_cell + direction
            while self.is_valid(curr_cell):
                if direction.row != 0:   # vertical
                    self.__shape[curr_cell.row][curr_cell.col] = '│'
                else:                    # horizontal
                    self.__shape[curr_cell.row][curr_cell.col] = '─'
                curr_cell = curr_cell + direction

    def __str__(self) -> str:
        output = ''
        for row in self.__shape:
            output = '\n'.join([output, ' '.join([str(item) for item in row])])
        return output


def main():
    size: int = 11

    shape = Shape(size)
    shape.get_plus(size)
    print(shape)

if __name__ == '__main__':
    main()