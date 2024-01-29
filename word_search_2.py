board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
words = ["oath", "pea", "eat", "rain", "ate"]


def findWords(board, words):
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.is_word = False

    class Trie:
        def __init__(self):
            self.root = TrieNode()

        def add(self, word):
            curr_node = self.root
            for char in word:
                if char not in curr_node.children:
                    curr_node.children[char] = TrieNode()
                curr_node = curr_node.children[char]
            curr_node.is_word = True

    trie = Trie()
    for word in words:
        trie.add(word)

    m = len(board)
    n = len(board[0])
    visited = set()
    l = []

    def traverse(i, j, node, visited, s):
        if not node.children.get(board[i][j]) and len(visited) != 0:
            return

        if node.children.get(board[i][j]):
            s += board[i][j]
            visited.add((i, j))
            if node.children[board[i][j]].is_word:
                l.append(s)

            new_node = node.children[board[i][j]]

            if i + 1 <= m - 1 and (i + 1, j) not in visited:
                traverse(i + 1, j, new_node, visited, s)

            if j + 1 <= n - 1 and (i, j + 1) not in visited:
                traverse(i, j + 1, new_node, visited, s)

            if i - 1 >= 0 and (i - 1, j) not in visited:
                traverse(i - 1, j, new_node, visited, s)

            if j - 1 >= 0 and (i, j - 1) not in visited:
                traverse(i, j - 1, new_node, visited, s)

            visited.remove((i, j))

            if len(s) > 1: return

        if i == m - 1 and j == n - 1:
            return

        if j < n - 1:
            traverse(i, j + 1, node, visited, "")

        elif i < m - 1:
            traverse(i + 1, 0, node, visited, "")

    traverse(0, 0, trie.root, visited, "")
    return list(set(l))


# board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
# words = ["oath", "pea", "eat", "rain", "ate"]
print(findWords(board, words))
