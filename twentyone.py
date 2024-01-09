import random


class GameState:
    def __init__(self, turn, sticks, latest_move):
        self.turn = turn
        self.sticks = sticks
        self.latest_move = latest_move

class PLayer:
    def __init__(self, name, banned):
        self.name = name
        self.banned = banned


def choose_mode():
    """
    Have user choose the game mode, responds with description and
    :return mode: corresponding mode number
    """
    while True:
        try:
            mode = int(input("Choose a mode:\n"
                             "1: Standard\n"
                             "2: Banned\n"))
            break
        except ValueError:
            print("Invalid input, please use number")
    match mode:
        case 1:
            print("Welcome to the 21 game.\n"
                  "There are 21 sticks, each turn you may take 1, 2, or 3 sticks.\n"
                  "The person to make the last legal move wins.\n")
        case 2:
            print("Welcome to the 21 game, banned version.\n"
                  "There are 21 sticks, each turn you may take 1, 2, or 3 sticks.\n"
                  "However, you may not make a move that is banned by your opponent.\n"
                  "The person to make the last legal move wins.\n")
    return mode


def game_order():
    """
    Have user choose whether to go first or second
    :return order: 1 = user go first, -1 = user go second
    """
    while True:
        query = input("Go first (y/n)?")
        if query.lower().strip() in ["y", "yes"]:
            order = 1
            break
        elif query.lower().strip() in ["n", "no"]:
            order = -1
            break
        else:
            print("Invalid input")
    return order


def player_turn(banned):
    while True:
        try:
            sticks_taken = int(input("Take how many sticks (1, 2, or 3)?"))
            if 1 <= sticks_taken <= 3  and sticks_taken != banned:
                break
        except ValueError:
            print("Invalid input")
        else:
            print("Invalid move, please enter only 1, 2 or 3")
    return sticks_taken


def standard_bot(sticks_left):
    """
    The bot will attempt to reduce the number of sticks left to a multiple of 4, always.
    If it can't (number of sticks is already a multiple of 4), it will randomly move
    """
    if sticks_left % 4 != 0:
        move = sticks_left % 4
    else:
        move = random.randrange(1, 3)
    return move


def twentyone_bot_ban(sticks_left, banned):
    """
    TODO: The math behind the bot—try just random moves first with check for bannings
    """


def main():
    current_player = ""
    mode = choose_mode()
    order = game_order()

    game = GameState(order, 21, 0)
    while game.sticks > 0:
        match game.turn:
            case 1:
                current_player = "Player"
                game.latest_move = player_turn(0)
                print(f"You took {game.latest_move} stick(s)")
            case -1:
                current_player = "Bot"
                game.latest_move = standard_bot(game.sticks)
                print(f"The bot took {game.latest_move} stick(s)")
        if game.sticks - game.latest_move < 0:
            print(f"There's not enough sticks, there's only {game.sticks} stick(s) left")
            continue
        game.sticks = game.sticks - game.latest_move
        print(f"There are {game.sticks} sticks left\n"
              "---------------------------")
        game.turn = game.turn * -1
    print(f"The {current_player} won")


if __name__ == '__main__':
    main()
