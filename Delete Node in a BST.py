def deleteNode(root, key):
  curr_node = root 
  prev = root
  if curr_node == None:
      return root
  while curr_node != None:
      if curr_node.val == key:
          if curr_node.left == None and curr_node.right == None:    #Deleting a leaf node
              if prev != curr_node:
                  if prev.left != None:
                      if prev.left.val == key:
                          prev.left = None
                  if prev.right != None:
                      if prev.right.val == key:
                          prev.right = None
              else:
                  root = None
              curr_node = None
          elif curr_node.left == None:  #Deleting a node with one child only
              if prev != curr_node:
                  if prev.left != None:
                      if prev.left.val == key:
                          prev.left = curr_node.right
                  if prev.right != None:
                      if prev.right.val == key:
                          prev.right = curr_node.right
              else:
                  root = curr_node.right
              curr_node = None
          elif curr_node.right == None: #Deleting a node with one child only
              if prev != curr_node:
                  if prev.left != None:
                      if prev.left.val == key:
                          prev.left = curr_node.left
                  if prev.right != None:
                      if prev.right.val == key:
                          prev.right = curr_node.left
              else:
                  root = curr_node.left
              curr_node = None
          else:                         #Deleting a node with two children
              sub_prev = None
              sub_curr = curr_node.right
              while sub_curr.left != None:
                  sub_prev = sub_curr
                  sub_curr = sub_curr.left
              curr_node.val = sub_curr.val
              if sub_prev != None:
                  sub_prev.left = sub_curr.right
              else:
                  curr_node.right = sub_curr.right
              break
              
      elif key < curr_node.val:
          prev = curr_node
          curr_node = curr_node.left
      else:
          prev = curr_node
          curr_node = curr_node.right
      
  return root
