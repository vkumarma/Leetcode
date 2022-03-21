def reverseList(head):
  current = head
  prev = None
  while current != None:
      temp = current
      current = temp.next
      temp.next = prev
      prev = temp
      
  head = prev
  return head


