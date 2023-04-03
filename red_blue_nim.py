import sys

RED_MULTIPLIER = 2
BLUE_MULTIPLIER = 3


def print_board(red_marbles, blue_marbles):
    print(f"Red: {red_marbles}, Blue: {blue_marbles}")


def get_user_move(red_marbles, blue_marbles):
    while True:
        pile = input("Select a pile to remove from (red/blue): ")
        if pile.lower() == "red" and red_marbles > 0:
            return "red"
        elif pile.lower() == "blue" and blue_marbles > 0:
            return "blue"
        else:
            print("Invalid move. Try again.")


def get_computer_move(red_marbles, blue_marbles):
    if red_marbles > blue_marbles:
        return "red"
    elif blue_marbles > red_marbles:
        return "blue"
    else:
        return "red"  # If both piles have the same number of marbles, remove from red


def update_board(pile, red_marbles, blue_marbles):
    if pile == "red":
        red_marbles -= 1
    else:
        blue_marbles -= 1
    return red_marbles, blue_marbles


def calculate_score(red_marbles, blue_marbles):
    return red_marbles * RED_MULTIPLIER + blue_marbles * BLUE_MULTIPLIER


def red_blue_nim(red_marbles, blue_marbles, first_player="computer"):
    current_player = first_player
    while red_marbles > 0 and blue_marbles > 0:
        print_board(red_marbles, blue_marbles)
        if current_player == "computer":
            pile = get_computer_move(red_marbles, blue_marbles)
            print("Computer removes 1 from", pile)
        else:
            pile = get_user_move(red_marbles, blue_marbles)
        red_marbles, blue_marbles = update_board(
            pile, red_marbles, blue_marbles)
        current_player = "computer" if current_player == "human" else "human"
    print_board(red_marbles, blue_marbles)
    score = calculate_score(red_marbles, blue_marbles)
    if red_marbles == 0:
        print("\nBlue wins with a score of", score)
        print("The winner is ", current_player)
    else:
        print("\nRed wins with a score of", score)
        print("The winner is ", current_player)


if __name__ == "__main__":
    # args = sys.argv[1:]
    # if len(args) < 2:
    #     print("Usage: red_blue_nim.py <num-red> <num-blue> [<first-player>]")
    #     sys.exit(1)
    # red_marbles = int(args[0])
    # blue_marbles = int(args[1])
    # first_player = "computer"
    # if len(args) > 2 and args[2].lower() == "human":
    #     first_player = "human"
    # red_blue_nim(red_marbles, blue_marbles, first_player)
    red_blue_nim(5, 7, "human")
