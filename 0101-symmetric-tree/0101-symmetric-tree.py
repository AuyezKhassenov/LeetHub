# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append([root.left, root.right])
        
        while q:
            left, right = q.pop()
            
            if not left and not right:
                continue
            if not left or not right:
                return False
            
            if left.val == right.val:
                q.append([left.left, right.right])
                q.append([left.right, right.left])
            else:
                return False
        
        return True
            
        
        