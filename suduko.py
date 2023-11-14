#!/usr/bin/env python3

board = [[".","7","3","2",".",".",".","4","9"], [".","4",".",".",".",".","7",".","."],
          [".",".",".",".",".","9","6",".","."], ["8",".",".","3",".",".",".",".","."],
          [".","6",".",".",".","2",".","5","1"], [".",".",".",".",".",".","9",".","."],
          [".","5",".",".",".","1",".","2","4"], [".",".",".",".",".",".",".","7","."],
          [".",".","6",".","5",".",".",".","."]]


for r1 in board:
    print(r1)
print("\n")


rows = len(board)
cols = len(board[0])
boxes = []
missing = []
known_set = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}

for l in board:
    new = known_set - set(l)
    missing.append(list(new))

i = 0
while i < 3:
    temp = i * 3
    box = {}
    for c in range(cols):
        if c % 3 == 0 and c != 0:
            boxes.append(box)
            box = {}

        for k in range(3):
            r = temp + k
            box[(r, c)] = board[r][c]

    boxes.append(box)
    i += 1


def traverse(board, i, j, miss, original, simp):
    if board[i][j] == '.':
        current_box = {}
        for b in boxes:
            if b.get((i, j)):
                current_box = b
                break

        for m in range(len(miss)):
            temp1 = miss[m]
            up = False
            down = False

            if temp1 not in current_box.values():
                for a in range(i, rows):
                    if temp1 == board[a][j]:
                        down = True  # fuck this loop

                if down: continue
                for d in range(i, -1, -1):
                    if temp1 == board[d][j]:
                        up = True

                if up: continue
                board[i][j] = temp1
                current_box[(i, j)] = temp1
                new_missing = miss[:m] + miss[m + 1:]
                if i == rows - 1 and j == cols - 1:
                    simp.pop()
                    return

                if j < cols - 1:
                    traverse(board, i, j + 1, new_missing, original, simp)

                elif i < rows - 1:
                    traverse(board, i + 1, 0, original[i + 1], original, simp)

                if len(simp) == 0: return
                board[i][j] = "."
                current_box[(i, j)] = "."

        return

    if i == rows - 1 and j == cols - 1:
        simp.pop()
        return

    if j < cols - 1:
        traverse(board, i, j + 1, miss, original, simp)
    elif i < rows - 1:
        traverse(board, i + 1, 0, original[i + 1], original, simp)


simp = [False]
traverse(board, 0, 0, missing[0], missing, simp)

for r in board:
    print(r)

for i in range(5):
    print("\n")