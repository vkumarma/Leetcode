class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def maxDepth(self, root):
  if root == None:
      return 0

  left_height = self.maxDepth(root.left)
  right_height = self.maxDepth(root.right)
      
  max_height = max(left_height, right_height) + 1
  return max_height