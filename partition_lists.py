def partition(head, x):
  if head == None:
      return head
  
  head_less = None
  tail_less = head_less
  
  head_greater = None
  tail_greater = head_greater
  
  current = head
  while current != None:
      next_node = current.next
      
      if current.val < x:
          if head_less == None:
              head_less = current
              tail_less = head_less
          else:
              tail_less.next = current
              tail_less = tail_less.next
      else:
          if head_greater == None:
              head_greater = current
              tail_greater = head_greater
              
          else:
              tail_greater.next = current
              tail_greater = tail_greater.next
          
      current.next = None
      current = next_node
  
  
  if head_less == None:
      return head_greater
  
  tail_less.next = head_greater
  
  return head_less