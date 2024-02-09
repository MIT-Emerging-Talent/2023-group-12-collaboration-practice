def generate_words(board, word_dict):
    def dfs(i, j, current_word):
        if i < 0 or i >= rows or j < 0 or j >= cols or visited[i][j]:
            return

        current_word += board[i][j]

        if current_word in word_dict:
            generated_words.add(current_word)

        visited[i][j] = True

        for x in range(-1, 2):
            for y in range(-1, 2):
                dfs(i + x, j + y, current_word)

        visited[i][j] = False

    if not board or not board[0] or not word_dict:
        return []

    rows, cols = len(board), len(board[0])
    visited = [[False] * cols for _ in range(rows)]
    generated_words = set()

    for i in range(rows):
        for j in range(cols):
            dfs(i, j, "")

    return list(generated_words)