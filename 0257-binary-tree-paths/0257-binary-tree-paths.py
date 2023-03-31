# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def dfs(root, path):
            
            if not root.left and not root.right:
                res.append(path.copy() + [root.val])
                return
           
            if root.left:
                dfs(root.left, path + [root.val])
            if root.right:
                dfs(root.right, path + [root.val])
        dfs(root, [])
        return ['->'.join([str(char) for char in p]) for p in res]
            
                
        