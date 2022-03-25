class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def insertIntoBST(root, val):  #Assuming no duplicates.
  new_node = TreeNode(val)
  node = root
  if node == None:
      root = new_node
      return root
  while(True):
      if new_node.val < node.val:
          if node.left == None:
              node.left = new_node
              break
          else:
              node = node.left
      elif new_node.val > node.val:
          if node.right == None:
              node.right = new_node
              break
          else:
              node = node.right
  
  return root