class ListNode:
  def __init__(self, val=0, next=None):
      self.val = val
      self.next = next
      
def sortList(head):  # mergesort used to sort linked list
  if head == None:
      return head
  def middle_node(head):  # finding middle node using fast and slow pointer.
      prev = None
      slow = head
      fast = head
      while fast.next != None:
          prev = slow
          slow = slow.next
          fast = fast.next.next
          if fast == None:
              break
      
      prev.next = None
      return slow
  
  def merge(left,right):  # creating new linked list / merging
      curr_left = left
      curr_right = right
      head = None
      while curr_left != None and curr_right != None:
          if curr_left.val > curr_right.val:
              if head == None:
                  head = curr_right
                  current = head
              else:
                  current.next = curr_right
                  current = current.next
              curr_right = curr_right.next
          else:
              if head == None:
                  head = curr_left
                  current = head
              else:
                  current.next = curr_left
                  current = current.next
              curr_left = curr_left.next
              
      if curr_left != None:
          current.next = curr_left
      elif curr_right != None:
          current.next = curr_right
      return head
  
  def mergesort(head):
      if head.next == None:  # if single node then just return head.
          return head
      mid_node = middle_node(head)
      right = mid_node 
      left = head
      
      left = mergesort(left)
      right = mergesort(right)
      
      return merge(left,right)
  
  return mergesort(head)