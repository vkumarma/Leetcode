# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        from collections import deque
        if head == None or head.next == None:
            return head

        num_nodes = 0
        d = deque()
        current = head
        while current != None:
            d.append(current)
            num_nodes += 1
            current = current.next

        if k > num_nodes:
            k = k % num_nodes

        while k != 0:
            last_node = d.pop()
            second_last_node = d.pop()
            second_last_node.next = None
            d.append(second_last_node)
            last_node.next = head
            head = last_node
            d.appendleft(last_node)
            k -= 1

        return d.popleft()
