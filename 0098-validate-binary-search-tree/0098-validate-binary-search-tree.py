# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, minVal, maxVal):
            
            if node and (node.val <= minVal or node.val >= maxVal):
                return False
            if node.left:
                left = dfs(node.left, minVal, node.val)
            else: 
                left = True
            if node.right:
                right = dfs(node.right, node.val, maxVal)
            else:
                right = True
            
            return left and right
        
        return dfs(root, float('-infinity'), float('infinity'))
            
        
        