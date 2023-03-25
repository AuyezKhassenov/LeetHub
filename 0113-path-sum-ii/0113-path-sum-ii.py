# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        
        def dfs(root, targetSum, tmp):
            if not root:
                return None
            
            if not root.left and not root.right and targetSum - root.val == 0:
                tmp.append(root.val)
                res.append(tmp)
                
              
            dfs(root.left, targetSum - root.val, tmp + [root.val])
            dfs(root.right, targetSum - root.val, tmp + [root.val])
            
        dfs(root, targetSum, [])
        return res
            
            
        