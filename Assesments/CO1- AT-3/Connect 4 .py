import math
import random

ROWS = 6
COLS = 7

EMPTY = 0
PLAYER = 1
AI = 2

board = [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]


def print_board():
    print()
    for row in board:
        print("|", end="")
        for cell in row:
            if cell == PLAYER:
                print(" X ", end="")
            elif cell == AI:
                print(" O ", end="")
            else:
                print(" . ", end="")
        print("|")
    print("  0  1  2  3  4  5  6")


def is_valid(col):
    return board[0][col] == EMPTY


def get_next_row(col):
    for r in range(ROWS - 1, -1, -1):
        if board[r][col] == EMPTY:
            return r


def drop_piece(row, col, piece):
    board[row][col] = piece


def winning(piece):

    # Horizontal
    for r in range(ROWS):
        for c in range(COLS - 3):
            if (board[r][c] == piece and
                board[r][c+1] == piece and
                board[r][c+2] == piece and
                board[r][c+3] == piece):
                return True

    # Vertical
    for r in range(ROWS - 3):
        for c in range(COLS):
            if (board[r][c] == piece and
                board[r+1][c] == piece and
                board[r+2][c] == piece and
                board[r+3][c] == piece):
                return True

    # Positive diagonal
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if (board[r][c] == piece and
                board[r+1][c+1] == piece and
                board[r+2][c+2] == piece and
                board[r+3][c+3] == piece):
                return True

    # Negative diagonal
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if (board[r][c] == piece and
                board[r-1][c+1] == piece and
                board[r-2][c+2] == piece and
                board[r-3][c+3] == piece):
                return True

    return False


def valid_locations():
    return [c for c in range(COLS) if is_valid(c)]


def score_position(piece):

    score = 0

    # Center column preference
    center = [board[r][COLS//2] for r in range(ROWS)]
    score += center.count(piece) * 3

    return score


def minimax(depth, alpha, beta, maximizing):

    valid = valid_locations()

    if winning(AI):
        return (None, 1000000)

    if winning(PLAYER):
        return (None, -1000000)

    if depth == 0 or len(valid) == 0:
        return (None, score_position(AI))

    if maximizing:

        value = -math.inf
        column = random.choice(valid)

        for col in valid:

            row = get_next_row(col)
            board[row][col] = AI

            new_score = minimax(depth-1, alpha, beta, False)[1]

            board[row][col] = EMPTY

            if new_score > value:
                value = new_score
                column = col

            alpha = max(alpha, value)

            if alpha >= beta:
                break

        return column, value

    else:

        value = math.inf
        column = random.choice(valid)

        for col in valid:

            row = get_next_row(col)
            board[row][col] = PLAYER

            new_score = minimax(depth-1, alpha, beta, True)[1]

            board[row][col] = EMPTY

            if new_score < value:
                value = new_score
                column = col

            beta = min(beta, value)

            if alpha >= beta:
                break

        return column, value


print("CONNECT FOUR AI")
print("You = X")
print("Computer = O")

print_board()

turn = PLAYER

while True:

    if turn == PLAYER:

        col = int(input("Enter column (0-6): "))

        if is_valid(col):

            row = get_next_row(col)
            drop_piece(row, col, PLAYER)

            print_board()

            if winning(PLAYER):
                print("You Win!")
                break

            turn = AI

    else:

        print("AI Thinking...")

        col, score = minimax(4, -math.inf, math.inf, True)

        row = get_next_row(col)
        drop_piece(row, col, AI)

        print_board()

        if winning(AI):
            print("AI Wins!")
            break

        turn = PLAYER

    if len(valid_locations()) == 0:
        print("Match Draw!")
        break
