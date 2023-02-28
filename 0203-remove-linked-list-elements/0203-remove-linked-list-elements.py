# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
            
        dummy = a = head
        
        while a:
        
            while a.next and a.next.val == val:
                a.next = a.next.next
            a = a.next
            
        return dummy
        