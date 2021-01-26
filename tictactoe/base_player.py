from abc import ABC, abstractmethod
from tictactoe.board import Point


class Player(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def move(self) -> Point:
        pass

    @property
    @abstractmethod
    def symbol(self) -> Point:
        pass
