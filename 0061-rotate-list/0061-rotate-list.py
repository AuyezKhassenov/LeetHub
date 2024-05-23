# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        l = 1
        tail = head
        while tail.next:
            l += 1
            tail = tail.next
         
        k = k % l
        if k == 0:
            return head
        dummy = head
        for _ in range(l - k - 1):
            dummy = dummy.next
        res = dummy.next
        
        dummy.next = None
        tail.next = head
        
        return res
        