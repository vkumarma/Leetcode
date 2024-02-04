def solveNQueens(n):
    a = ["."]
    board = [a * n for i in range(n)]
    l = []

    def check(board, pos):
        r, c = pos
        while r < n:
            if board[r][c] == "Q":
                return False
            r += 1

        r, c = pos
        while r >= 0:
            if board[r][c] == "Q":
                return False
            r -= 1

        r, c = pos
        while c < n:
            if board[r][c] == "Q":
                return False
            c += 1

        r, c = pos
        while c >= 0:
            if board[r][c] == "Q":
                return False
            c -= 1

        r, c = pos
        while r < n and c < n:
            if board[r][c] == "Q":
                return False
            r += 1
            c += 1

        r, c = pos
        while r >= 0 and c >= 0:
            if board[r][c] == "Q":
                return False
            r -= 1
            c -= 1

        r, c = pos
        while r < n and c >= 0:
            if board[r][c] == "Q":
                return False
            r += 1
            c -= 1

        r, c = pos
        while r >= 0 and c < n:
            if board[r][c] == "Q":
                return False
            r -= 1
            c += 1

        return True

    def traverse(board, i):
        if i >= n:
            temp = ["".join(board[b]) for b in range(n)]
            l.append(temp)
            return

        for j in range(0, n):
            if check(board, (i, j)):
                board[i][j] = "Q"
                traverse(board, i + 1)
                board[i][j] = "."

    traverse(board, 0)
    return l


print(solveNQueens(4))  # [['.Q..', '...Q', 'Q...', '..Q.'], ['..Q.', 'Q...', '...Q', '.Q..']]
print(solveNQueens(5))



