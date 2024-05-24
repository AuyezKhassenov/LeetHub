# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        rev = None
        
        while slow:
            tmp = slow.next
            slow.next = rev
            rev, slow = slow, tmp

            
        while rev:
            if rev.val != head.val:
                return False
            rev, head = rev.next, head.next
        return True