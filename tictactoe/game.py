from tictactoe.board import Board, PointOccupiedException, Point, X, O
from itertools import cycle
from tictactoe.base_player import Player
from typing import List, Tuple, Union
# Static type aliases
PlayerList = List[Player]
CandidateList = List[List[List[int]]]

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

    def __init__(self, players: PlayerList):
        self._board = Board()
        self._candidate_wins = list(self.POSSIBLE_WINS)
        self._players = players

    @property
    def players(self) -> PlayerList:
        return self._players

    @property
    def board(self) -> Board:
        return self._board

    @property
    def candidate_wins(self) -> CandidateList:
        return self._candidate_wins
    
    def remove_candidate(self, candidate: List[List[int]]) -> bool:
        if (candidate in self._candidate_wins):
            self._candidate_wins.remove(candidate)
            return True
        return False

    def add_player(self, player: Player):
        self._players.append(player)

    def _check_line(self, candidate, ply_type) -> Tuple[bool, Union[Point, X, O]]:
        hits = [cell for cell in self._board.flat_view() if type(cell) is ply_type and [cell.x, cell.y] in candidate]
        return (len(hits) == 3 and ply_type is not Point, ply_type)

    def _check(self) -> Tuple[bool, Union[Point, X, O]]:
        """
           Check the state of the board, return tuple containing game status and winning player
        """
        for winstate in self.candidate_wins:
            for player in self.players:
                win, player = self._check_line(candidate=winstate, ply_type=player.symbol)
                if win:
                    return (True, player)

        return (False, None)

    def run(self) -> bool:
        for player in cycle(self._players):
            while True:
                print("Board:", self._board, sep="\n")
                try:
                    move = player.move()
                    self._board.board = move
                except PointOccupiedException:
                    print("[!!!] Illegal move, try again")
                    continue
                except KeyboardInterrupt:
                    print(f"\nPlayer {player.name} gives up!")
                    return
                else: 
                    break
            
            win, player_type = self._check()
            if self.board.is_full() and not win:
                print("Board:", self._board, sep="\n")
                print("It's a draw!")
                return False

            if win:
                player_name = [ply.name for ply in self.players if ply.symbol == player_type].pop()
                print("Board:", self._board, sep="\n")
                print(f"{player_name} wins!")
                return True
