# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        l = []
        while head:
            l.append(head.val)
            head = head.next
        
        def build_tree(l):
            if not l:
                return None
            
            m = len(l) // 2
            
            root = TreeNode(l[m])
            
            root.left = build_tree(l[:m])
            root.right = build_tree(l[m+1:])
            
            return root
        
        return build_tree(l)
        