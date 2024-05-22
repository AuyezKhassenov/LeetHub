# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def cycle_len(end):
            step = 0
            start = end
            while True:
                start = start.next
                step += 1
                if start is end:
                    return step
                
        fast = slow = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                cycled_node = head
                for _ in range(cycle_len(slow)):
                    cycled_node = cycled_node.next
                
                it = head 
                
                while it is not cycled_node:
                    it, cycled_node = it.next, cycled_node.next
                    
                return it
        