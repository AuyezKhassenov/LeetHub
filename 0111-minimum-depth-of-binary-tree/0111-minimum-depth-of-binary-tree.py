# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        elif not root.right:
            right = float('inf')
            left = self.minDepth(root.left)
        elif not root.left:
            left = float('inf')
            right = self.minDepth(root.right)
        else:
            right = self.minDepth(root.right)
            left = self.minDepth(root.left)
        return 1 + min(right, left)