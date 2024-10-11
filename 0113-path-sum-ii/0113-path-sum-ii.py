# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.ans = []
        
        def dfs(node, cur_sum, cur_list):

            if node:
                
                if not node.left and not node.right and cur_sum == node.val:
                    cur_list.append(node.val)
                    self.ans.append(cur_list)
                    
                dfs(node.left, cur_sum - node.val, cur_list + [node.val])
                dfs(node.right, cur_sum - node.val, cur_list + [node.val])
        

        dfs(root, targetSum, [])
        return self.ans
                
