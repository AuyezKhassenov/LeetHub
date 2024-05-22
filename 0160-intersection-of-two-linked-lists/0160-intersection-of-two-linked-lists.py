# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def length_list(node):
            l = 0
            while node:
                l += 1
                node = node.next
            return l
        
        A_len, B_len = length_list(headA), length_list(headB)
        
        if A_len < B_len:
            headA, headB = headB, headA
        
        for _ in range(abs(A_len - B_len)):
            headA = headA.next
        
        while headB and headA and headB is not headA:
            headB, headA = headB.next, headA.next
        
        return headB