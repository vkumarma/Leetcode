class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def mergeTrees(root1,root2):
    
  if root2 == None and root1 != None:
      return root1
  elif root2 != None and root1 == None:
      return root2

  def dfs(root1,root2):
      if root1 != None and root2 != None:
          root1.val = root1.val + root2.val

      if root1 == None or root2 == None:
          return
      if root1.left == None:
          root1.left = root2.left
          root2.left = None

      if root1.right == None:
          root1.right = root2.right
          root2.right = None
  

      dfs(root1.left,root2.left)
      dfs(root1.right,root2.right)

      return root1
  return dfs(root1,root2)