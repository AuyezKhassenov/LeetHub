# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        i = 0
        cur = head
        while cur:
            cur = cur.next
            i += 1
            if i > 10001:
                return True
        '''
        
        
        try:
            slow, fast = head, head.next
            while True:
                fast = fast.next.next
                slow = slow.next
                if slow == fast:
                    return True
        except:
            return False
            