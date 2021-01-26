from typing import List, Union


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"[{self.x},{self.y}]"


class X(Point):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __str__(self) -> str:
        return "X"


class O(Point):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __str__(self) -> str:
        return "O"


class PointOccupiedException(Exception):
    pass


class Board:

    def __init__(self):
        self._board = list()
        for y in range(3):
            self._board.append(list())
            for x in range(3):
                self._board[y].append(Point(x, y))

    @property
    def board(self) -> List[List[int]]:
        return self._board

    @board.setter
    def board(self, val: Union[X, O]):
        try:
            if type(self._board[val.y][val.x]) is Point:
                self._board[val.y][val.x] = val
                return
        except IndexError:
            pass
        raise PointOccupiedException("unable to move to occupied cell", val)

    def is_full(self) -> bool:
        return len([1 for row in self._board for cell in row if type(cell) is Point]) == 0

    def get_cell(self, coords: List[int]) -> Union[Point, X, O]:
        return self.board[coords[0]][coords[1]]

    def flat_view(self) -> List[Union[Point, X, O]]:
        return [cell for row in self.board for cell in row]

    def __str__(self) -> str:
        """
        | X | O |   |
        | O |   |   |
        |   | X |   |
        """
        board_str = ""
        for line in self._board:
            board_str += f"|\t{line[0]}\t|\t{line[1]}\t|\t{line[2]}\t|\n"
        return board_str
