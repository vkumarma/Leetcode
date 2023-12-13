#!/usr/bin/env python3
def exist(board, word) -> bool:
    l = [False]
    m = len(board)
    n = len(board[0])
    act_len = len(word)
    visited = set()
    
    def traverse(i, j, word, l, visited):
        
        if len(l) == 0: return 

        if len(word) != 0:
            if word[0] == board[i][j]:
                visited.add((i,j))
                temp = word[1:]
                
                if len(temp) == 0:
                    l.pop()
                    return
                    
                if i+1 <= m-1 and (i+1,j) not in visited: 
                    traverse(i+1, j, temp, l, visited)

                if j+1 <= n-1 and (i,j+1) not in visited: 
                    traverse(i, j+1, temp, l, visited)

                if i-1 >= 0 and (i-1,j) not in visited: 
                    traverse(i-1, j, temp, l, visited)

                if j-1 >= 0 and (i,j-1) not in visited: 
                    traverse(i, j-1, temp, l, visited)

                visited.remove((i,j))

            
            if len(word) < act_len:
                return

        else:
            l.pop()
            return 


        if i == m - 1 and j == n - 1:
            return

        if j < n - 1: 
            traverse(i, j+1, word,l, visited)

        elif i < m - 1: 
            traverse(i+1, 0, word, l, visited)
    
    traverse(0, 0, word, l, visited)

    if len(l) == 0: return True
    else: return False

print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "DFS"))
print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
