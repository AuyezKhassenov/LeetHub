# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        while True:
            
            if root.val == p.val:
                return p
            elif root.val == q.val:
                return q
            elif p.val < root.val < q.val or p.val > root.val > q.val:
                return root
            elif root.val > p.val and root.val > q.val:
                root = root.left
            else:
                root = root.right
        
            