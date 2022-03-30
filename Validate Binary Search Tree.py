class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def isValidBST(self, root: Optional[TreeNode]) -> bool:
  from collections import deque
  q = deque()
  node = root
  q.appendleft(node)
  while len(q) != 0:
      temp = q.pop()
      if temp.left != None:
          node = temp.left
          while node.right != None:
              node = node.right
          if node.val >= temp.val:
              return False
          q.appendleft(temp.left)
      if temp.right != None:
          node = temp.right
          while node.left != None:
              node = node.left
          if node.val <= temp.val:
              return False
          q.appendleft(temp.right)
  
  return True