# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        node = head
        even = dummy_even = ListNode(0, None)

        while node and node.next:
            even.next = node.next
            even = even.next
            if node.next.next:
                node.next = node.next.next
            else:
                break
            node = node.next
            even.next = None
            
        node.next = dummy_even.next
        return head