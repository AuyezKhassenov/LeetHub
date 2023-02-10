# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root):
        res = []
        if root:
            res.append(root.val)
            res = res + self.helper(root.left)
            res = res + self.helper(root.right)
        return res
        
        
        
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        temp = self.helper(root)
        temp.sort()
        res = 100000
        for i in range(len(temp)-1):
            res = min(res, temp[i+1] - temp[i])
        return res
        