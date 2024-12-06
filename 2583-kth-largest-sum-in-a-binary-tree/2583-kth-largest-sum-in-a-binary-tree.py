# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        res = defaultdict(int)
        def dfs(node, level):
            if not node:
                return
            res[level] += node.val
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        dfs(root,0)
        return sorted(res.values(), reverse=True)[k-1] if k <= len(res.values()) else -1