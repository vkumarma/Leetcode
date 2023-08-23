# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return 
        if head.next == None or k == 1:
            return head
        

        size = 0
        current = head
        while current != None:
            size += 1
            current = current.next

        l = [None, head] # p1,c1
        c2 = head
        p2 = None
        index = 1
        a = 0
        l2 = []

        def reverse(l, c2, p2, index, a, l2):
            if index >= k: # 3 == 3
                return 
            
            p2 = c2
            c2 = c2.next
            index += 1
            reverse(l, c2, p2, index, a, l2)
            # swapping 
            if len(l) != 0:
                c1 = l.pop()
                p1 = l.pop()
                
                l.append(c2) # new p1
                l.append(c1.next) # new  c1
                
                if index > (k // 2): # index >= mid
                    if c1 != c2:
                        temp = c2.next
                        if p1 == None:
                            if c1 == p2:
                                c1.next = temp
                                c2.next = c1
                                head = c2
                            else:
                                c2.next = c1.next
                                c1.next = temp
                                p2.next = c1
                                head = c2
                                
                            l2.append(head)
                        else:
                            if c1 == p2:
                                c2.next = c1
                                c1.next = temp
                                p1.next = c2
                            else:
                                c2.next = c1.next
                                p2.next = c1
                                c1.next = temp
                                p1.next = c2
                            
    
            if index != 2:
                return
            a += 1
            if a < (size // k): 
                temp = c2
                index = 1
                return reverse([temp.next, temp.next.next], temp.next.next, temp.next, index, a, l2) 

            return l2.pop()
                
        return reverse(l, c2, p2, index, a, l2)

