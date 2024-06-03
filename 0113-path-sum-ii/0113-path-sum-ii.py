# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.ans = []
        def dfs(node, sum_nodes, res):
            if not node:
                return
            
            sum_nodes += node.val
            res = res + [node.val]
            
            if not node.left and not node.right and sum_nodes == targetSum:
                self.ans.append(res)
                return
            
            dfs(node.left, sum_nodes, res)
            dfs(node.right, sum_nodes, res)
        
        dfs(root, 0, [])
        return self.ans
                