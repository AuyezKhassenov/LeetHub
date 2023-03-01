# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverseList(head):
            prev, cur = None, head
            
            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            
            return prev
        
        fast = slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        rev = reverseList(slow)
        
        while rev:
            if rev.val != head.val:
                return False
            rev = rev.next
            head = head.next
        
        return True
        