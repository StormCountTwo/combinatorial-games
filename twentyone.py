import random


class GameState:
    def __init__(self, turn, sticks, latest_move):
        self.turn = turn
        self.sticks = sticks
        self.latest_move = latest_move


def player_turn():
    while True:
        try:
            sticks_taken = int(input("Take how many sticks (1, 2, or 3)?"))
            if 1 <= sticks_taken <= 3:
                break
        except ValueError:
            print("Invalid input")
        else:
            print("Invalid move, please enter only 1, 2 or 3")
    return sticks_taken


def twentyone_bot(sticks_left, opponent_move):
    """
    :param sticks_left: Number of sticks left
    :param opponent_move: What did opponent just do?
    :return move: How many sticks the bot will take
    """
    if sticks_left % 4 != 0:
        move = sticks_left % 4
    else:
        move = random.randrange(1, 3)
    return move

def main():
    game_order = 0
    while True:
        query = input("Go first (y/n)?")
        if query.lower().strip() in ["y", "yes"]:
            game_order = 1
            break
        elif query.lower().strip() in ["n", "no"]:
            game_order = -1
            break
        else:
            print("Invalid input")

    game = GameState(game_order, 21, 0)
    while game.sticks > 0:
        match game.turn:
            case 1:
                current_player = "Player"
                print("It is the player's turn")
                game.latest_move = player_turn()
                print(f"You took {game.latest_move} stick(s)")
            case -1:
                current_player = "Bot"
                print("It is the bot's turn")
                game.latest_move = twentyone_bot(game.sticks, game.latest_move)
                print(f"The bot took {game.latest_move} stick(s)")
        if game.sticks - game.latest_move < 0:
            print(f"There's not enough sticks, there's only {game.sticks} stick(s) left")
            continue
        game.sticks = game.sticks - game.latest_move
        print(f"There are {game.sticks} sticks left\n")
        game.turn = game.turn * -1
    print(f"The {current_player} won")


if __name__ == '__main__':
    main()
