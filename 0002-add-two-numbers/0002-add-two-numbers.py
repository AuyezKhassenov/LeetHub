# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rem = 0
        
        dummy = start = ListNode()
        
        while l1 and l2:
            res = l1.val + l2.val + rem
            if res >= 10:
                res = res - 10
                start.next = ListNode(res)
                rem = 1
                
            else:
                start.next = ListNode(res)
                rem = 0
            
            start = start.next
            l1 = l1.next
            l2 = l2.next
        
        l3 = l1 or l2
        print(l3)
        while l3:
            res = l3.val + rem
            if res >= 10:
                res = res - 10
                start.next = ListNode(res)
                rem = 1
                
            else:
                start.next = ListNode(res)
                rem = 0
            
            l3 = l3.next
            start = start.next
        if rem == 1:
            start.next = ListNode(1)
            
        return dummy.next
            
        
        