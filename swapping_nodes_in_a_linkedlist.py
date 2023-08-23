# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head == None:
            return 
        if head.next == None:
            return head

        size = 0
        current = head
        p1 = None
        p2 = None
        c1 = head 
        c2 = None

        while current != None:
            size += 1
            current = current.next
        
        f = k-1
        s = size - k
        if f < s:
            index = s
            f = f
        elif f > s:
            index = f
            f = s
        else:
            index = f

        for i in range(0, index):
            if index!=f:
                if i == f:
                    c2 = c1
                    p2 = p1
            
            p1 = c1
            c1 = c1.next
        
        if c2 == None:
            return head
        elif p2 == None:
            temp = c1.next
            if c2 == p1:
                c2.next = temp
                c1.next = c2
                head = c1
            else:
                c1.next = c2.next
                c2.next = temp
                p1.next = c2
                head = c1
        else:
            temp = c1.next
            if c2 == p1:
                c1.next = c2
                c2.next = temp
                p2.next = c1
            else:
                c1.next = c2.next
                p1.next = c2
                c2.next = temp
                p2.next = c1
        return head
        
