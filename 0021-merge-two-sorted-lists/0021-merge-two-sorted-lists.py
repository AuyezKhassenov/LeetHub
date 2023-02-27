class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        
        dummy = res = ListNode()
        
        while list1 and list2:
            if list1.val <= list2.val:
                res.next = list1
                list1 = list1.next
                
            else:
                res.next = list2
                list2 = list2.next
            res = res.next
        
        res.next = list1 or list2
                    
            
        return dummy.next