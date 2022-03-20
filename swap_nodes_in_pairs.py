def swapPairs(head):
  if head == None or head.next == None:
      return head
  
  index = 0
  current = head
  prev = None
  while current != None:
      if index % 2 != 0:
          if index != 1:
              temp = current
              prev.next.next = current.next
              temp.next = prev.next
              prev.next = temp
          else:
              temp = current
              head.next = current.next
              temp.next = head
              head = temp
          prev = current.next
          current = prev
      index += 1
      current = current.next
      
  return head

