# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node, num_bin):
            if not node:
                return
            
            num_bin = num_bin + str(node.val)
            
            if not node.left and not node.right:
                self.ans += int(num_bin, 2)
                return
            
            dfs(node.left, num_bin)
            dfs(node.right, num_bin)
            
        dfs(root, '')
        return self.ans