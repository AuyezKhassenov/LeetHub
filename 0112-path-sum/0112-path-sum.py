# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        q = deque()
        q.append([root, targetSum - root.val])

        while q:
            node, sumLeft = q.popleft()
            
            if node:
                if not node.left and not node.right and sumLeft == 0:
                    return True
                
                if node.left:
                    q.append([node.left, sumLeft - node.left.val])
                if node.right:
                    q.append([node.right, sumLeft - node.right.val])
                         
        return False            
        