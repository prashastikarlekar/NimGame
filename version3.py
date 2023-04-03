import sys

RED_MULTIPLIER = 2
BLUE_MULTIPLIER = 3


def evaluate_state(num_red, num_blue, is_maximizing):
    if num_red == 0 or num_blue == 0:
        # game has ended, return score
        if is_maximizing:
            return -BLUE_MULTIPLIER * num_blue
        else:
            return -RED_MULTIPLIER * num_red
    else:
        # game still ongoing, return heuristic score
        return BLUE_MULTIPLIER * num_blue - RED_MULTIPLIER * num_red


def minmax_alpha_beta(num_red, num_blue, depth, alpha, beta, is_maximizing):
    if depth == 0 or num_red == 0 or num_blue == 0:
        return evaluate_state(num_red, num_blue, is_maximizing)

    if is_maximizing:
        max_eval = -sys.maxsize
        for color in ['red', 'blue']:
            if color == 'red':
                if num_red > 0:
                    eval_score = minmax_alpha_beta(
                        num_red-1, num_blue, depth-1, alpha, beta, False)
                    max_eval = max(max_eval, eval_score)
                    alpha = max(alpha, eval_score)
            else:
                if num_blue > 0:
                    eval_score = minmax_alpha_beta(
                        num_red, num_blue-1, depth-1, alpha, beta, False)
                    max_eval = max(max_eval, eval_score)
                    alpha = max(alpha, eval_score)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = sys.maxsize
        for color in ['red', 'blue']:
            if color == 'red':
                if num_red > 0:
                    eval_score = minmax_alpha_beta(
                        num_red-1, num_blue, depth-1, alpha, beta, True)
                    min_eval = min(min_eval, eval_score)
                    beta = min(beta, eval_score)
            else:
                if num_blue > 0:
                    eval_score = minmax_alpha_beta(
                        num_red, num_blue-1, depth-1, alpha, beta, True)
                    min_eval = min(min_eval, eval_score)
                    beta = min(beta, eval_score)
            if beta <= alpha:
                break
        return min_eval


def get_human_move(num_red, num_blue):
    while True:
        pile = input("Choose a pile to remove from (red/blue): ")
        if pile.lower() not in ['red', 'blue']:
            print("Invalid pile choice. Please try again.")
            continue
        num_marbles = input("How many marbles would you like to remove? ")
        if not num_marbles.isdigit():
            print("Invalid input. Please try again.")
            continue
        num_marbles = int(num_marbles)
        if (pile.lower() == 'red' and num_marbles > num_red) or (pile.lower() == 'blue' and num_marbles > num_blue):
            print("Not enough marbles in chosen pile. Please try again.")
            continue
        return pile.lower(), num_marbles


def red_blue_nim(num_red, num_blue, first_player='computer', depth=None):
    print(f"Current Score is RED: {num_red} and BLUE : {num_blue}")

    while num_red > 0 and num_blue > 0:
        if first_player.lower() == 'computer':
            print(f"*****************Computer's turn:*****************")
            max_eval = -sys.maxsize
            max_move = None
            for color in ['red', 'blue']:
                if color == 'red':
                    if num_red > 0:
                        eval_score = minmax_alpha_beta(
                            num_red-1, num_blue, depth, -sys.maxsize, sys.maxsize, False)
                        if eval_score > max_eval:
                            max_eval = eval_score
                            max_move = (color, 1)
                        else:
                            continue
                    else:
                        if num_blue > 0:
                            eval_score = minmax_alpha_beta(
                                num_red, num_blue-1, depth, -sys.maxsize, sys.maxsize, False)
                            if eval_score > max_eval:
                                max_eval = eval_score
                                max_move = (color, 1)
                            else:
                                continue
                    print(
                        f"Computer chooses to remove 1 {max_move[0]} marble.")

                    if max_move[0] == 'red':
                        num_red -= 1
                    else:
                        num_blue -= 1
                    print(
                        f"Current Score is RED: {num_red} and BLUE : {num_blue}")
                    first_player = 'human'
        else:
            print(f"*****************Human's turn:*****************\n")
            pile, num_marbles = get_human_move(num_red, num_blue)
            if pile == 'red':
                num_red -= num_marbles
            else:
                num_blue -= num_marbles
            print(f"Human removes {num_marbles} {pile} marble(s).")
            print(f"Current Score is RED: {num_red} and BLUE : {num_blue}")
            first_player = 'computer'

    if num_red == 0 or num_blue == 0:
        # winner = 'Computer'
        if first_player == "human":
            winner = 'computer'
        else:
            winner = 'human'
        winner = winner.upper()
        if num_blue == 0 and num_red != 0:
            score = num_red * RED_MULTIPLIER
        if num_red == 0 and num_blue != 0:
            score = num_blue * BLUE_MULTIPLIER

    print(
        f"\n*****************{winner} wins with a score of {score}!*****************")


def main():
    num_red = 4
    num_blue = 4
    first_player = 'human'
    depth = 4

    # num_red = int(sys.argv[1])

    # num_blue = int(sys.argv[2])
    # first_player = 'computer' if len(
    #     sys.argv) < 4 or sys.argv[3] == 'computer' else 'human'
    # depth = int(sys.argv[4]) if len(sys.argv) == 5 else 4

    red_blue_nim(num_red, num_blue, first_player, depth)


if __name__ == '__main__':
    main()
