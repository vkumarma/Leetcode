class TrieNode(object):
  def __init__(self):
      self.is_word = False
      self.children = {}
class Trie:

  def __init__(self):
      self.root = TrieNode()

  def insert(self, word: str) -> None:
      current_node = self.root 
      for i in range(len(word)):
          if word[i] not in current_node.children:
              new_node = TrieNode()
              if i == len(word) - 1:
                  new_node.is_word = True
              current_node.children[word[i]] = new_node
              current_node = new_node
          else:
              current_node = current_node.children[word[i]]
              if i == len(word) - 1:
                  current_node.is_word = True
      

  def search(self, word: str) -> bool:
      current_node = self.root
  
      for char in word:
          if char not in current_node.children:
              return False

          current_node = current_node.children[char]

      return current_node.is_word

  def startsWith(self, prefix: str) -> bool:
      current_node = self.root
  
      for char in prefix:
          if char not in current_node.children:
              return False

          current_node = current_node.children[char]

      return True
        

a = ["insert", "search", "search", "startsWith", "insert", "search"]
b = ["apple", "apple", "app", "app","app", "app"]

trie = Trie()
for i in range(0,len(a)):
  if a[i] == "insert":
    print(trie.insert(b[i]))
  elif a[i] == "search":
    print(trie.search(b[i]))
  else:
    print(trie.startsWith(b[i]))
    