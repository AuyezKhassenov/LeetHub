# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        def traverse(node):
            if node:
                traverse(node.left)
                self.ans.append(node.val)
                traverse(node.right)
        traverse(root)
        return self.ans