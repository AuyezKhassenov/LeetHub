# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def _sum(node):
            if not node:
                return 0
            left = _sum(node.left)
            right = _sum(node.right)
            
            self.res += abs(left - right)
            return node.val + left + right
        _sum(root)
        return self.res
                
        