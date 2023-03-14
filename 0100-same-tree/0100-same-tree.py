# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.res = True
        def dfs(node1, node2):
            first = node1.val if node1 else 10001
            second = node2.val if node2 else 10001
            if first != second:
                self.res = False
            if node1 and node2:
                dfs(node1.left, node2.left)
                dfs(node1.right, node2.right)
            return
        dfs(p,q)
        return self.res
            
            