# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = []
        def dfs(node, num):
            
            if not node:
                return
            
            num = num*10 + node.val
            if not node.left and not node.right:
                self.ans.append(num)
            
            dfs(node.left, num)
            dfs(node.right, num)
        dfs(root, 0)
        return sum(self.ans)