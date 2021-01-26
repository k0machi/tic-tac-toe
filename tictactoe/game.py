from tictactoe.board import Board, PointOccupiedException, Point
from itertools import cycle


class Game:

    POSSIBLE_WINS = [
        # horizontals
        [[0,0], [1,0], [2,0]],
        [[0,1], [1,1], [2,1]],
        [[0,2], [1,2], [2,2]],
        # verticals
        [[0,0], [0,1], [0,2]],
        [[1,0], [1,1], [1,2]],
        [[2,0], [2,1], [2,2]],
        # diagonals
        [[0,0], [1,1], [2,2]],
        [[0,2], [1,1], [2,0]],
    ]

    def __init__(self, players):
        self._board = Board()
        self._players = players

    @property
    def players(self):
        return self._players

    @property
    def board(self):
        return self._board
    def _check_line(self, winstate, ply_type):
        hits = [cell for line in self._board.board for cell in line if type(cell) is ply_type and [cell.x, cell.y] in winstate]
        return (len(hits) == 3 and ply_type is not Point, ply_type)

    def _check(self):
        """
           If the game ends return list of winners, else empty list []
        """
        return []

        for winstate in self.POSSIBLE_WINS:
            for player in self.players:
                win, player = self._check_line(winstate, ply_type=player.symbol)
                if win:
                    return (True, player)

        return (False, None)

    def run(self):
        for player in cycle(self._players):
            move = player.move()
            self._board.board = move
            print(self._board)
            winners = self._check()
            if winners:
                # print winners
                return
