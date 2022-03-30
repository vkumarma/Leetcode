class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def pathSum(root, targetSum):
  res = []
  visited = []
  if root == None:
      return res
  def dfs(root, res):
      node = root
      visited.append(node.val)
      if node.left == None and node.right== None:
          if sum(visited) == targetSum:
              res += [visited[:]]
      else:
          if node.left != None:
              dfs(node.left,res)

          if node.right != None:
              dfs(node.right,res)
              
      visited.pop()
      return 
  dfs(root,res)
  return res