# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        
        if not root:
            return 0
        
        q.append([root, 1])
        
        while q:
            node, level = q.popleft()
            
            if not node.left and not node.right:
                return level
            
            if node.left:
                q.append([node.left, level + 1])
            if node.right:
                q.append([node.right, level + 1])
            
            
            