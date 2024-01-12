import random


class Player:
    def __init__(self, name, banned):
        self.name = name
        self.banned = banned


def yes_or_no(question):
    while True:
        y_or_n = input(f"{question} (y/n)? ")
        if y_or_n.lower().strip() in ["y", "yes"]:
            yn_bool = True
            break
        elif y_or_n.lower().strip() in ["n", "no"]:
            yn_bool = False
            break
        else:
            print("Invalid input")
    return yn_bool


def choose_mode():
    """
    Have user choose the game mode, responds with description of the mode
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
            print("Work in progress. Please choose another mode")
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
    """
    Let use configure the parameters for custom mode
    :return min_move, max_move, sticks:
    """
    while True:
        try:
            min_move = int(input("Choose the MINIMUM number of sticks that can be taken: "))
            max_move = int(input("Choose the MAXIMUM number of sticks that can be taken: "))
            sticks = int(input("Choose the starting number of sticks for the game: "))
            break
        except ValueError:
            print("Invalid Input, Please try again")
    return min_move, max_move, sticks


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


def banned_bot(sticks_left, banned):
    """
    TODO: The math behind the bot—try just random moves first with check for banning
    """


def custom_bot(sticks_left, min_move, max_move):
    """
    Bot that can win in custom cases
    """
    current_mod = sticks_left % (min_move + max_move)
    print(current_mod)
    # Check if bot has guaranteed path to victory
    if min_move <= current_mod:
        print("i can win")
        # Bot has guaranteed path for victory
        if current_mod <= max_move:
            move = current_mod
        else:
            move = random.randrange(2*max_move - current_mod, max_move)
    else:
        print("i random")
        # Bot doesn't have guaranteed path for victory, randomly moves
        move = random.randrange(min_move, max_move)
    return move


def run_game(mode, sticks, min_move, max_move, order):
    current_player = ""
    latest_move = 0
    while sticks >= min_move:
        match order:
            case 1:
                current_player = "Player"
                latest_move = player_turn(0, min_move, max_move)
                print(f"You took {latest_move} stick(s)")
            case -1:
                current_player = "Bot"
                match mode:
                    case 1:
                        latest_move = standard_bot(sticks)
                    case 2:
                        print("WIP")
                    case 3:
                        latest_move = custom_bot(sticks, min_move, max_move)
                print(f"The bot took {latest_move} stick(s)")
        if sticks - latest_move < 0:
            print(f"There's not enough sticks, there's only {sticks} stick(s) left")
            continue
        sticks = sticks - latest_move
        print(f"There are {sticks} sticks left\n"
              "---------------------------")
        order = order * -1
    print(f"The {current_player} won")


def main():
    min_move = 0
    max_move = 0
    sticks = 0
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
    while True:
        if yes_or_no("Do you want to go first"):
            order = 1
        else:
            order = -1
        run_game(mode, sticks, min_move, max_move, order)
        if yes_or_no("Do you want to play again"):
            if yes_or_no("Configure a new game\n"):
                print("---------------------------")
                main()
        else:
            print("Goodbye")
            break


if __name__ == '__main__':
    main()
