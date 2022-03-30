class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def sumNumbers(root):
  s = ""
  res = []
  def dfs(root,res,s):
      node = root
      s += str(node.val)
      if node.left == None and node.right == None:
          temp = 0
          if len(res) != 0:
              temp = res.pop()
          res.append(temp + int(s))
      else:
          if node.left != None:
              dfs(root.left,res,s)
          if node.right != None:
              dfs(root.right,res,s)
      
      return 
  dfs(root,res,s)
  return res.pop()