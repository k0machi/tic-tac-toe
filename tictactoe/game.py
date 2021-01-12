from tictactoe.board import Board
from itertools import cycle


class Game:
    def __init__(self, players):
        self._board = Board()
        self._players = players

    @property
    def players(self):
        return self._players

    def _check(self):
        """
           If the game ends return list of winners, else empty list []
        """
        return []

    def run(self):
        for player in cycle(self._players):
            move = player.move()
            self._board.board = move
            print(self._board)
            winners = self._check()
            if winners:
                # print winners
                return
