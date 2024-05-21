# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = sublist_head = ListNode(0, head)
        for _ in range(1, left):
            sublist_head = sublist_head.next
            
        sublist_iter = sublist_head.next
        for _ in range(right-left):
            tmp = sublist_head.next
            # sublist_iter.next = tmp.next
            # tmp.next = sublist_iter.next
            # sublist_head.next = 
            sublist_head.next = sublist_iter.next
            sublist_iter.next = sublist_iter.next.next
            sublist_head.next.next = tmp
            
        return dummy.next
            
                