from tictactoe.game import Game
from tictactoe.player import HumanPlayer
from tictactoe.board import X, O


def main_human():
    game = Game(players=[
        HumanPlayer(name="Fedor", symbol_class=X),
        HumanPlayer(name="Julia", symbol_class=O),
    ])
    Game(players="Bentsi")
    game.run()


def main_robotic():
    """Robot plays with Robot"""
    pass


def main_robotic_human():
    """Robot plays with Human"""
    pass


if __name__ == '__main__':
    main_human()
    main_robotic()
    main_robotic_human()
