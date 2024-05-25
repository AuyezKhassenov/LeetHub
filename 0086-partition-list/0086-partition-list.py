# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        start = dummy_start = ListNode(0)
        end = dummy_end = ListNode(0)
        
        while head:
            if head.val < x:
                start.next = head
                start = start.next
            else:
                end.next = head
                end = end.next
                
            head=head.next
        start.next, end.next = None, None

        
        if dummy_start.next:
            start.next = dummy_end.next
        elif dummy_end.next:
            dummy_start.next = dummy_end.next
            
        return dummy_start.next