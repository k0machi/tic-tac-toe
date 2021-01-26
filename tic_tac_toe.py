from tictactoe.game import Game
from tictactoe.player import HumanPlayer, RoboticPlayer
from tictactoe.board import X, O
from itertools import cycle


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


def main():
    print("pycrosses, v1.0")
    try:
        while True:
            while True:
                try:
                    human_players = int(input("How many human players? [2]> "))
                    human_players = human_players if human_players <= 2 else 2
                    break
                except ValueError:
                    print("Not a number")

            player_names = [
                input(f"Enter player {i + 1} name> ") for i in range(human_players)]

            game = Game(players=[])
            symbols = cycle([X, O])
            for v in player_names:
                game.add_player(HumanPlayer(
                    name=v, symbol_class=next(symbols)))

            for _ in range(2 - human_players):
                game.add_player(RoboticPlayer(
                    symbol_class=next(symbols), gamestate=game))

            game.run()
            answer = input("Play again? y/n> ")
            if (answer == 'y'):
                continue
            break
    except EOFError:
        exit(1)
    except KeyboardInterrupt:
        exit(1)


if __name__ == '__main__':
    main()
