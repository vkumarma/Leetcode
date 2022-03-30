class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def minDiffInBST(root):
  from collections import deque
  q = deque()
  min_distance = float("inf")
  node = root
  q.appendleft(node)
  distance_left = float("inf")
  distance_right = float("inf")
  while len(q) != 0:
      temp = q.pop()
      if temp.left != None:
          node = temp.left
          while node.right != None:
              node = node.right
          distance_left = temp.val - node.val
          q.appendleft(temp.left)
      if temp.right != None:
          node = temp.right
          while node.left != None:
              node = node.left
          distance_right = node.val - temp.val
          q.appendleft(temp.right)
      
      current_min = min(distance_left,distance_right)
      min_distance = min(min_distance,current_min)
  
  return min_distance