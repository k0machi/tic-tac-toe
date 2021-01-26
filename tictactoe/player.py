from abc import ABC, abstractmethod

from tictactoe.board import X


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
    pass


if __name__ == '__main__':
    player = HumanPlayer(name="Fedor", symbol_class=X)
    print(player.move())