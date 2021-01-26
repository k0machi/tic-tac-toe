class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"[{self.x},{self.y}]"


class X(Point):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __str__(self):
        return "X"


class O(Point):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __str__(self):
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
    def board(self):
        return self._board

    @board.setter
    def board(self, val):
        if not isinstance(self._board[val.y][val.x], X) and not isinstance(self._board[val.y][val.x], O):
            self._board[val.y][val.x] = val
            return
        raise PointOccupiedException("unable to move to occupied cell", val)

    def is_full(self):
        return len([1 for row in self._board for cell in row if type(cell) is Point])== 0

    def __str__(self):
        """
        | X | O |   |
        | O |   |   |
        |   | X |   |
        """
        board_str = ""
        for line in self._board:
            board_str += f"|\t{line[0]}\t|\t{line[1]}\t|\t{line[2]}\t|\n"
        return board_str
