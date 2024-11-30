# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def dfs(node, cur_sum, cur_list):
            if not node:
                return
            
            cur_sum += node.val
            cur_list.append(node.val)
            
            if not node.left and not node.right:
                if cur_sum == targetSum:
                    ans.append(cur_list[:])
                    
            dfs(node.left, cur_sum, cur_list)
            dfs(node.right, cur_sum, cur_list)
            
            cur_list.pop()
        
        dfs(root, 0, [])
        return ans