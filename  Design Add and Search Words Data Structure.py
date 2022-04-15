class TrieNode(object):
  def __init__(self):
    self.is_word = False
    self.children = {}
        
class WordDictionary:
  def __init__(self):
    self.root = TrieNode()

  def addWord(self, word: str) -> None:
    curr_node = self.root
    for char in word:
        if char not in curr_node.children:
            curr_node.children[char] = TrieNode()
        curr_node = curr_node.children[char]
    curr_node.is_word = True
        
  def search(self, word: str) -> bool:
    curr_node = self.root
    def dfs(curr_node,word):
        for char in word:
            if char == ".":
                for key in curr_node.children:
                    curr_n = curr_node.children[key]
                    if dfs(curr_n,word[1:]) == True:
                        return True
            elif char in curr_node.children:
                curr_n = curr_node.children[char]
                if dfs(curr_n,word[1:]) == True:
                    return True
            return 
        if curr_node.is_word == True:
            return True
        
    if dfs(curr_node,word):
        return True
    else:
        return False
            
                        
                        
                        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)