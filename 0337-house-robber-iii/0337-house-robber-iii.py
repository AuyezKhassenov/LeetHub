# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0, 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            one = left[0] + right[0]
            two = left[1] + right[1]
            tmp = max(node.val + two, one)
            two = one
            one = tmp
            
            return one, two
        return max(dfs(root))
        