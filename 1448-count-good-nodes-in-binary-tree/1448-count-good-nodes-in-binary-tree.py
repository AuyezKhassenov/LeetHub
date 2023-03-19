# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maxVal):
            
            if not node:
                return 0
            
            
            if node.left:
                left = dfs(node.left, max(maxVal, node.left.val))
            else:
                left = 0
                
            if node.right:
                right = dfs(node.right, max(maxVal, node.right.val))
            else:
                right = 0
                
            if node.val >= maxVal:
                return 1 + left + right
            else:
                return left + right
            
        
        return dfs(root, root.val)
            
            
        