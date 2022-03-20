def deleteDuplicates(head):
  hash = {}
  current = head
  previous = None
  while current != None:
      if hash.get(current.val):
          if previous != None:
              previous.next = current.next
      else:
          hash[current.val] = True
          previous = current
      current = current.next 
  return head

