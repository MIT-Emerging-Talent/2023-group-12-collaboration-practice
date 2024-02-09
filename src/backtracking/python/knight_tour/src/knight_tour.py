def is_valid_move(x, y, n, visited):
    return 0 <= x < n and 0 <= y < n and not visited[x][y]

def count_accessible_squares(x, y, n, visited):
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
             (-2, -1), (-1, -2), (1, -2), (2, -1)]
    
    count = 0
    for move in moves:
        new_x, new_y = x + move[0], y + move[1]
        if is_valid_move(new_x, new_y, n, visited):
            count += 1
    
    return count

def knight_tour(n):
    # Initialize the chessboard and visited array
    chessboard = [[-1 for _ in range(n)] for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]

    # Initial position of the knight
    start_x, start_y = 0, 0
    chessboard[start_x][start_y] = 1
    visited[start_x][start_y] = True

    # Perform the Knight's Tour using Warnsdorff's Rule
    for move_number in range(2, n * n + 1):
        current_x, current_y = start_x, start_y
        min_accessible_squares = float('inf')
        next_x, next_y = -1, -1

        # Check all possible moves
        for move in [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]:
            new_x, new_y = current_x + move[0], current_y + move[1]
            if is_valid_move(new_x, new_y, n, visited):
                accessible_squares = count_accessible_squares(new_x, new_y, n, visited)
                if accessible_squares < min_accessible_squares:
                    min_accessible_squares = accessible_squares
                    next_x, next_y = new_x, new_y

        # If no valid moves are found, the Knight's Tour is not possible
        if next_x == -1 and next_y == -1:
            return None

        # Make the next move
        chessboard[next_x][next_y] = move_number
        visited[next_x][next_y] = True
        start_x, start_y = next_x, next_y

    return chessboard

# Example usage for a 5x5 chessboard
result = knight_tour(5)
if result:
    for row in result:
        print(row)
else:
    print("No solution exists.")
