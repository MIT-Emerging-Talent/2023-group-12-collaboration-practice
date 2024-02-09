def evaluate(board):
    # Check rows, columns, and diagonals for a win or loss
    for row in board:
        if all(cell == 'X' for cell in row):
            return 1  # Player 'X' wins
        elif all(cell == 'O' for cell in row):
            return -1  # Player 'O' wins

    for col in range(3):
        if all(board[row][col] == 'X' for row in range(3)):
            return 1
        elif all(board[row][col] == 'O' for row in range(3)):
            return -1

    if all(board[i][i] == 'X' for i in range(3)) or all(board[i][2 - i] == 'X' for i in range(3)):
        return 1
    elif all(board[i][i] == 'O' for i in range(3)) or all(board[i][2 - i] == 'O' for i in range(3)):
        return -1

    # Check for a draw
    if all(cell != ' ' for row in board for cell in row):
        return 0  # Draw

    return None  # The game is still ongoing

def minimax(board, depth, maximizing_player):
    score = evaluate(board)

    if score is not None:
        return score

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = ' '  # Undo the move
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = ' '  # Undo the move
                    min_eval = min(min_eval, eval)
        return min_eval

def find_best_move(board):
    best_val = float('-inf')
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                move_val = minimax(board, 0, False)
                board[i][j] = ' '  # Undo the move

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

# Example usage:
initial_board = [['X', 'O', ' '],
                 ['X', 'O', ' '],
                 [' ', ' ', ' ']]

best_move = find_best_move(initial_board)
print("Optimal move:", best_move)
