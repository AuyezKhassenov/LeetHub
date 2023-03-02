# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:


        #print(head)
        """
        Do not return anything, modify head in-place instead.
        """
        def reverseList(head: Optional[ListNode]) -> ListNode():
            prev, cur = None, head
            
            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            
            return prev
        
        slow, fast = head, head.next
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        second = slow.next
          
        rev = reverseList(second)
        
        first, second_2 = head, rev
        
        while second_2:
            tmp1, tmp2 = first.next, second_2.next
            first.next = second_2
            second_2 = tmp1
            first, second_2 = tmp1, tmp2
'''           
class Solution:
    def reorderList(self, head: ListNode) -> None:
        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
            

            
            
        
        