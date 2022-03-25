def levelOrder(root):
  from collections import deque
  level = 0
  visit_order = []
  new_l = []
  q = deque()
  node = root
  if node == None:
      return visit_order
  
  q.appendleft((node,level))
  while len(q) != 0: # BFS used for level order traversal 
      temp, level = q.pop()
      visit_order.append(([temp.val],level))
      if temp.left != None: 
          q.appendleft((temp.left,level+1))
      if temp.right != None:
          q.appendleft((temp.right,level+1))
          
  previous_level = -1
  for i in range(0,len(visit_order)):  
      node, level = visit_order[i]
      if level == previous_level:
          n = new_l.pop() + node
          new_l.append(n)
      else:
          new_l.append(node)
          previous_level = level
          
  return new_l