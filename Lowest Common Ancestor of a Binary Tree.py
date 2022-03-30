class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
  visited = []
  ancestors = []
  res = 0
  def dfs(root,ancestors):
      node = root
      visited.append(node)
      if node.val == p.val or node.val == q.val:
          ancestors += [visited[:]]
        
      if node.left != None:
          dfs(node.left,ancestors)
      if node.right != None:
          dfs(node.right,ancestors)
              
      visited.pop()
      return 
  dfs(root,ancestors)
  
  if len(ancestors) > 1:
      l1 = ancestors[0]
      l2 = ancestors[1]
      for i in range(len(l1)):
          if i < len(l2):
              if l1[i] == l2[i]:
                  res = l1[i]
  else:
      res = ancestors[0].pop()
  
  return res