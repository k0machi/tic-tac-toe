from abc import ABC, abstractmethod

from tictactoe.board import X, O, Point
from tictactoe.game import Game


class Player(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @property
    @abstractmethod
    def symbol(self):
        pass


class HumanPlayer(Player):
    def __init__(self, name, symbol_class):
        self._name = name
        self._symbol_class = symbol_class

    @property
    def name(self):
        return self._name

    def move(self):
        symbol = self._symbol_class.__name__
        loc = input(f"[{self.name}] Where to set {symbol}? (use , to separate) ")
        x, y = loc.split(",")
        return self._symbol_class(x=int(x), y=int(y))

    @property
    def symbol(self):
        return self._symbol_class


class RoboticPlayer(Player):

    DIAGONAL_CELLS = [
        [0,0], [1,1], [2,2], 
        [0,2], [1,1], [2,0]
    ]

    def __init__(self, symbol_class, gamestate: Game):
        self._name = f"AI ({symbol_class.__name__})"
        self._symbol_class = symbol_class
        self._gamestate = gamestate

    @property
    def symbol(self):
        return self._symbol_class

    @property
    def name(self):
        return self._name

    def move(self):
        print(f"{self.name} is thinking...")
        opponent = [ply for ply in self._gamestate.players if ply != self]
        # Check for free cells nearing win state
        for ply in [self.symbol, opponent[0].symbol]:
            winstate = None
            for win in self._gamestate.POSSIBLE_WINS:
                cells = [cell for row in self._gamestate.board.board for cell in row if [cell.x, cell.y] in win]
                free_cells_remaining = [cell for cell in cells if type(cell) is Point]
                if (len(free_cells_remaining) == 1):
                    winstate = free_cells_remaining[0]
                    break
            if winstate:
                return self.symbol(x=winstate.x, y=winstate.y)
        
        # Check if center is free, occuppy if so
        center = self._gamestate.board.board[1][1]
        if type(center) is Point:
            return self.symbol(x=center.x, y=center.y)

        # Check first free diagonal cell
        for cell in self.DIAGONAL_CELLS:
            board_cell = self._gamestate.board.board[cell[0]][cell[1]]
            if type(board_cell) is Point:
                return self.symbol(x=board_cell.x, y=board_cell.y)
        
        # Default: return first free cell
        free_cell = [cell for row in self._gamestate.board.board for cell in row if type(cell) is Point]
        return self.symbol(x=free_cell.x, y=free_cell.y)
        

if __name__ == '__main__':
    player = HumanPlayer(name="Fedor", symbol_class=X)
    print(player.move())