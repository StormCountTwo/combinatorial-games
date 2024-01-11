import random


class Player:
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
                             "2: Banned\n"
                             "3: Custom\n"))
            break
        except ValueError:
            print("Invalid input, please use number")
    match mode:
        case 1:
            print("Welcome to the 21 game.\n"
                  "There are 21 sticks, each turn you may take 1, 2, or 3 sticks.\n"
                  "The player to make the last legal move wins.\n")
        case 2:
            print("Welcome to the 21 game, banned version.\n"
                  "There are 21 sticks, each turn you may take 1, 2, or 3 sticks.\n"
                  "However, you may not make a move that is banned by your opponent.\n"
                  "The player to make the last legal move wins.\n"
                  "Work in progress. Please choose another mode")
            choose_mode()
        case 3:
            print("Welcome to custom mode.\n"
                  "Here you can configure the rules of the game.\n"
                  "You can configure the minimum and maximum of sticks that can be taken\n"
                  "and the starting number of sticks.\n"
                  "The player to make the last legal move wins.\n")
        case _:
            print("Please choose a valid mode.")
            choose_mode()
    return mode


def custom_configure():
    while True:
        try:
            min_move= int(input("Choose the MINIMUM number of sticks that can be taken: "))
            max_move = int(input("Choose the MAXIMUM number of sticks that can be taken: "))
            sticks = int(input("Choose the starting number of sticks for the game: "))
            break
        except ValueError:
            print("Invalid Input, Please try again")
    return min_move, max_move, sticks


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


def player_turn(banned, min_move, max_move):
    """
    Have user choose a move with corresponding restrictions
    :param banned: What move is banned
    :param min_move: Min number of sticks to take
    :param max_move: Max number of sticks to take
    :return: The player's move
    """
    while True:
        try:
            sticks_taken = int(input(f"Take how many sticks ({min_move} - {max_move})?"))
            if min_move <= sticks_taken <= max_move and sticks_taken != banned:
                break
        except ValueError:
            print("Invalid input")
        else:
            print(f"Invalid move, please enter a number from {min_move} - {max_move}")
    return sticks_taken


def standard_bot(sticks_left, min_move, max_move):
    """
    The bot will attempt to reduce the number of sticks left to a multiple of 4, always.
    If it can't (number of sticks is already a multiple of 4), it will randomly move
    TODO: make it work for min_move != 1
    """
    if sticks_left % (max_move + 1) != 0:
        move = sticks_left % (max_move + 1)
    else:
        move = random.randrange(min_move, max_move)
    return move


def banned_bot(sticks_left, banned):
    """
    TODO: The math behind the bot—try just random moves first with check for bannings
    """


def main():
    current_player = ""
    min_move = 0
    max_move = 0
    sticks = 0
    latest_move = 0
    mode = choose_mode()
    match mode:
        case 1:
            min_move = 1
            max_move = 3
            sticks = 21
        case 2:
            print("meow")
            # WIP
        case 3:
            min_move, max_move, sticks = custom_configure()
    order = game_order()

    # TODO: Change win condition to last legal move made and not if there are no sticks left
    while sticks > 0:
        match order:
            case 1:
                current_player = "Player"
                latest_move = player_turn(0, min_move, max_move)
                print(f"You took {latest_move} stick(s)")
            case -1:
                current_player = "Bot"
                latest_move = standard_bot(sticks, min_move, max_move)
                print(f"The bot took {latest_move} stick(s)")
        if sticks - latest_move < 0:
            print(f"There's not enough sticks, there's only {sticks} stick(s) left")
            continue
        sticks = sticks - latest_move
        print(f"There are {sticks} sticks left\n"
              "---------------------------")
        order = order * -1
    print(f"The {current_player} won")


if __name__ == '__main__':
    main()
