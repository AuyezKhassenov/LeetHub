# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        while head:
            tmp = head
            
            while head.next and head.next.val == head.val:
                head = head.next
                
            tmp.next = head.next
            head = head.next
            
        return dummy