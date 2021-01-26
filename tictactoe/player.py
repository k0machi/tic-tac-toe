from tictactoe.board import X, O, Point
from tictactoe.game import Game
from tictactoe.base_player import Player
from random import choice
from typing import Union

class HumanPlayer(Player):
    def __init__(self, name: str, symbol_class: Point):
        self._name = name
        self._symbol_class = symbol_class

    @property
    def name(self) -> str:
        return self._name

    def move(self) -> Point:
        symbol = self._symbol_class.__name__
        while True:
            loc = input(f"[{self.name}] Where to set {symbol}? (use ',' to separate values)> ")
            try:
                x, y = loc.split(",")
            except ValueError:
                print("Invalid input")
                continue
            return self._symbol_class(x=int(x), y=int(y))

    @property
    def symbol(self) -> Point:
        return self._symbol_class


class RoboticPlayer(Player):

    DIAGONAL_CELLS = [
        [0,0], [1,1], [2,2], 
        [0,2], [1,1], [2,0]
    ]

    CENTER = [1, 1]

    def __init__(self, symbol_class: Point, gamestate: Game):
        self._name = f"AI ({symbol_class.__name__})"
        self._symbol_class = symbol_class
        self._gamestate = gamestate
        self._diagonals = list(self.DIAGONAL_CELLS)

    @property
    def symbol(self) -> Point:
        return self._symbol_class

    @property
    def name(self) -> str:
        return self._name

    def move(self) -> Point:
        print(f"[{self.name}] Thinking...")
        opponent = [ply for ply in self._gamestate.players if ply != self].pop()
        b = self._gamestate.board

        # Check for free cells nearing win state
        for ply in [self.symbol, opponent.symbol]:
            winstate = None
            for win in self._gamestate.candidate_wins:
                cells = [cell for cell in b.flat_view() if [cell.x, cell.y] in win]
                cells_occupied = [cell for cell in cells if type(cell) is ply]
                if (len(cells_occupied) == 2):
                    free_cells = [cell for cell in cells if type(cell) is Point]
                    if (len(free_cells) == 1):
                        winstate = free_cells.pop()
                        break
                    else:
                        # All cells are occupied, remove the candidate
                        # TODO: Maybe move it to Game::_check
                        self._gamestate.remove_candidate(win)
            if winstate:
                return self.symbol(x=winstate.x, y=winstate.y)
        
        # Check if center is free, occuppy if so
        center = b.get_cell(self.CENTER)
        if type(center) is Point:
            return self.symbol(x=center.x, y=center.y)

        # Check random free diagonal cell
        free_diagonals = [b.get_cell(cell) for cell in self._diagonals if type(b.get_cell(cell)) is Point]
        if len(free_diagonals) > 0:
            diag = choice(free_diagonals)
            self._diagonals.remove([diag.x, diag.y])
            return self.symbol(x=diag.x, y=diag.y)
        
        # Default: return first free cell
        free_cells = [cell for cell in b.flat_view() if type(cell) is Point]
        if len(free_cells) > 0:
            free_cell = free_cells[::-1].pop()
            return self.symbol(x=free_cell.x, y=free_cell.y)
        

if __name__ == '__main__':
    player = HumanPlayer(name="Fedor", symbol_class=X)
    print(player.move())