# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = dummy = ListNode(0)
        ten = 0
        while l1 or l2 or ten:
            first = l1.val if l1 else 0
            second = l2.val if l2 else 0
            summ = first + second + ten
            ten = summ // 10
            summ = summ % 10
            dummy.next = ListNode(summ)
            dummy = dummy.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            
        return res.next