import sys

# Returns the score of the given board state


def eval(board):
    red_score = board[0] * 2
    blue_score = board[1] * 3
    return red_score + blue_score

# Generates all possible moves for the given board state


def generate_moves(board):
    moves = []
    if board[0] > 0:
        moves.append(('red', 1))
    if board[1] > 0:
        moves.append(('blue', 1))
    return moves

# Returns the new board state after making a move


def make_move(board, move):
    new_board = board[:]
    if move[0] == 'red':
        new_board[0] -= move[1]
    else:
        new_board[1] -= move[1]
    return new_board

# MinMax algorithm with alpha-beta pruning


def minmax_alpha_beta(depth, board, maximizing_player, alpha, beta):
    if depth == 0 or board[0] == 0 or board[1] == 0:
        return None, eval(board)
    if maximizing_player:
        max_val = -sys.maxsize
        best_move = None
        for move in generate_moves(board):
            new_board = make_move(board, move)
            _, score = minmax_alpha_beta(
                depth-1, new_board, False, alpha, beta)
            if score > max_val:
                max_val = score
                best_move = move
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        return max_val, best_move[1]
    else:
        min_val = sys.maxsize
        best_move = None
        for move in generate_moves(board):
            new_board = make_move(board, move)
            _, score = minmax_alpha_beta(depth-1, new_board, True, alpha, beta)
            if score < min_val:
                min_val = score
                best_move = move
            beta = min(beta, score)
            if beta <= alpha:
                break
        return min_val, best_move[1]

# Play the red-blue nim game


def red_blue_nim(num_red, num_blue, first_player='computer', depth=4):
    board = [num_red, num_blue]
    current_player = first_player
    score = 0

    while True:
        print(f"Red: {board[0]}, Blue: {board[1]}")
        if current_player == 'computer':
            move, _ = minmax_alpha_beta(
                depth, board, True, -sys.maxsize, sys.maxsize)
            print(f"Computer removes {move[1]} from {move[0]}")
            board = make_move(board, move)
            if board[0] == 0 or board[1] == 0:
                break
            current_player = 'human'
        else:
            while True:
                pile = input("Select a pile to remove from (red/blue): ")
                if pile == 'red' and board[0] > 0:
                    break
                elif pile == 'blue' and board[1] > 0:
                    break
                else:
                    print("Invalid input!")
            while True:
                num = int(input("Select a number to remove: "))
                if (pile == 'red' and num <= board[0]) or (pile == 'blue' and num <= board[1]):
                    break
                else:
                    print("Invalid input!")
            board = make_move(board, (pile, num))
            if board[0] == 0 or board[1] == 0:
                break
            current_player = 'computer'

        print(f"\nCurrent State: Red={board[0]}, Blue={board[1]}\n")

        # Check if either pile is empty, declare the winner and exit
        if board[0] == 0:
            print("Red pile is empty. Computer wins!")
            score = 3 * board[1]
            break
        elif board[1] == 0:
            print("Blue pile is empty. Computer wins!")
            score = 2 * board[0]
            break

        if current_player == 'computer':
            print("Computer's turn...")
            _, move = minmax_alpha_beta(
                depth, board, True, float('-inf'), float('inf'))
            if move == 'red' and board[0] > 0:
                board[0] -= 1
                print(f"Computer removes 1 marble from {move} pile")
            else:
                board[1] -= 1
            print(f"Computer removes 1 marble from {move} pile")
            current_player = 'human'
        else:
            print("Human's turn...")
            pile = input("Select a pile to remove from (red/blue): ")
            while pile != 'red' and pile != 'blue':
                pile = input(
                    "Invalid input. Select a pile to remove from (red/blue): ")
            if pile == 'red':
                board[0] -= 1
            else:
                board[1] -= 1
            print(f"Human removes 1 marble from {pile} pile")
            current_player = 'computer'

    # Print the final score
    print(f"\nFinal Score:\nRed={board[0]}, Blue={board[1]}")
    if score > 0:
        print("Computer wins!")
    elif score < 0:
        print("Human wins!")
    else:
        print("It's a tie!")


def main():
    num_red = 5
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
