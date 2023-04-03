import sys

RED_MULTIPLIER = 2
BLUE_MULTIPLIER = 3


def evaluate_game_state(red_count, blue_count):
    """Evaluate the current game state and return the score for the current player."""
    return RED_MULTIPLIER * red_count + BLUE_MULTIPLIER * blue_count


def get_computer_move(red_count, blue_count, depth):
    """Use the Minimax algorithm with alpha-beta pruning to select the best move for the computer player."""
    best_score = float('-inf')
    best_move = None
    for pile, count in enumerate((red_count, blue_count)):
        # else other player has already won
        if count > 0:

            if pile == 0:
                new_red_count = red_count - 1
                new_blue_count = blue_count
            else:
                new_red_count = red_count
                new_blue_count = blue_count - 1

            score = min_value(new_red_count, new_blue_count,
                              depth - 1, float('-inf'), float('inf'))
            if score > best_score:
                best_score = score
                p = "blue"
                if pile == 0:
                    p = "red"
                best_move = (p, 1)
    return best_move


def min_value(red_count, blue_count, depth, alpha, beta):
    """Find the minimum score for the computer player."""
    if red_count == 0 or blue_count == 0:
        return evaluate_game_state(red_count, blue_count)
    if depth == 0:
        # Use a heuristic function to estimate the score when the search depth is reached.
        return 0
    for pile, count in enumerate((red_count, blue_count)):
        if count > 0:
            for i in range(1, count + 1):
                if pile == 0:
                    new_red_count = red_count - i
                    new_blue_count = blue_count
                else:
                    new_red_count = red_count
                    new_blue_count = blue_count - i
                score = max_value(new_red_count, new_blue_count,
                                  depth - 1, alpha, beta)
                beta = min(beta, score)
                if beta <= alpha:
                    return beta
    return beta


def max_value(red_count, blue_count, depth, alpha, beta):
    """Find the maximum score for the computer player."""
    if red_count == 0 or blue_count == 0:
        return evaluate_game_state(red_count, blue_count)
    if depth == 0:
        # Use a heuristic function to estimate the score when the search depth is reached.
        return 0
    for pile, count in enumerate((red_count, blue_count)):
        if count > 0:
            for i in range(1, count + 1):
                if pile == 0:
                    new_red_count = red_count - i
                    new_blue_count = blue_count
                else:
                    new_red_count = red_count
                    new_blue_count = blue_count - i
                score = min_value(new_red_count, new_blue_count,
                                  depth - 1, alpha, beta)
                alpha = max(alpha, score)
                if beta <= alpha:
                    return alpha
    return alpha


def get_human_move(red_count, blue_count):
    pile = None
    while pile not in ('red', 'blue'):
        pile = input("Select a pile (red or blue): ").lower()

    # max_count = red_count if pile == 'red' else blue_count
    # count = None
    # while count not in range(1, max_count + 1):
    #     count = input(f"Select a number of marbles to remove (1-{max_count}): ")
    #     try:
    #         count = int(count)
    #     except ValueError:
    #         count = None

    return pile, 1


def red_blue_nim(red_count, blue_count, first_player='computer', depth=None):
    # Initialize game state
    game_state = {'red': red_count, 'blue': blue_count}
    player = first_player
    score = {'human': 0, 'computer': 0}

    # Main game loop
    while True:
        # Print game state
        print(f"\nGame state: {game_state}")
        print(
            f"Score: human = {score['human']}, computer = {score['computer']}\n")

        # Check if game is over
        if game_state['red'] == 0 or game_state['blue'] == 0:
            winner = 'human' if player == 'computer' else 'human'
            final_score = score[winner] + 2 * \
                game_state['red'] + 3 * game_state['blue']
            print(f"\n{winner} wins with a score of {final_score}!")
            break

        # Get move for current player
        if player == 'computer':
            pile, count = get_computer_move(
                game_state['red'], game_state['blue'], depth)
            print(
                f"Computer selects pile '{pile}' and removes {count} marble(s).\n")
        else:
            pile, count = get_human_move(game_state['red'], game_state['blue'])
            print(
                f"Human selects pile '{pile}' and removes {count} marble(s).\n")

        # Update game state and score
        game_state[pile] -= count
        score[player] += 2 if pile == 'red' else 3

        # Switch players
        player = 'human' if player == 'computer' else 'computer'


def main():

    # if len(sys.argv) < 3:
    #     print("Usage: red_blue_nim.py <num-red> <num-blue> <first-player> <depth>")
    #     sys.exit(1)

    # # num_red = int(sys.argv[1])
    # # num_blue = int(sys.argv[2])
    # num_red = 5
    # num_blue = 4
    # first_player = "computer"
    # # if (len(sys.argv) >= 4):
    # #     first_player = sys.argv[3]

    # depth = None
    # if (len(sys.argv) == 5):
    #     depth = int(sys.argv[4])

    red_blue_nim(4, 4, 'human', depth=0)


if __name__ == "__main__":
    main()

    # Rest of your code goes here...
