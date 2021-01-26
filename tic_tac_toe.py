from tictactoe.game import Game
from tictactoe.player import HumanPlayer, RoboticPlayer
from tictactoe.board import X, O


def main_human():
    game = Game(players=[
        HumanPlayer(name="Fedor", symbol_class=X),
        HumanPlayer(name="Julia", symbol_class=O),
    ])
    game.run()


def main_robotic():
    game = Game(players=[])
    game.add_player(
        RoboticPlayer(symbol_class=X, gamestate=game)
    )
    game.add_player(
        RoboticPlayer(symbol_class=O, gamestate=game)
    )
    game.run()


def main_robotic_human():
    game = Game(players=[
        HumanPlayer(name="Fedor", symbol_class=X),
    ])
    game.add_player(
        RoboticPlayer(symbol_class=O, gamestate=game)
    )
    game.run()


if __name__ == '__main__':
    #main_human()
    main_robotic()
    #main_robotic_human()
