class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
      
def flatten(root):
  """
  Do not return anything, modify root in-place instead.
  """
  if root == None:
      return
  stack = []
  def dfs(root,stack):
    if root.left == None and root.right == None:
        stack.append(root)
        return 
    if root.right != None:
        root.left,root.right = root.right,root.left
    
    if root.left != None:
        dfs(root.left,stack)
        if root.right != None:
            dfs(root.right,stack)
            current = stack.pop()
            current.right = root.left
        else:
            root.right = root.left
        root.left = None
      
  dfs(root,stack)