import math

def evaluate(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != "_":
            return 10 if row[0] == "X" else -10
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "_":
            return 10 if board[0][col] == "X" else -10
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "_":
        return 10 if board[0][0] == "X" else -10
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "_":
        return 10 if board[0][2] == "X" else -10
    return 0

def is_moves_left(board):
    for row in board:
        if "_" in row:
            return True
    return False

def minmax(board, depth, is_max):
    score = evaluate(board)
    if score == 10:
        return score - depth
    if score == -10:
        return score + depth
    if not is_moves_left(board):
        return 0
    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == "_":
                    board[i][j] = "X"
                    best = max(best, minmax(board, depth + 1, False))
                    board[i][j] = "_"
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == "_":
                    board[i][j] = "O"
                    best = min(best, minmax(board, depth + 1, True))
                    board[i][j] = "_"
        return best

def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == "_":
                board[i][j] = "X"
                move_val = minmax(board, 0, False)
                board[i][j] = "_"
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move

board = [
    ["X", "O", "X"],
    ["_", "O", "_"],
    ["_", "_", "_"]
]

best_move = find_best_move(board)
print("The best move is:", best_move)
