class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = res = ListNode()
        
        while list1 and list2:
            if list1.val > list2.val:
                res.next = list2
                list2 = list2.next
            else:
                res.next = list1
                list1 = list1.next
            res = res.next
        if list1:
            res.next = list1
        if list2:
            res.next = list2
        
        return dummy.next
     