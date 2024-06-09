# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        val = preorder[0]
        root = TreeNode(val)
        idx = inorder.index(val)
        inorder_left = inorder[:idx]
        inorder_right = inorder[idx+1:]
        preorder_left = preorder[1:idx+1]
        preorder_right = preorder[idx+1:]

        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)
        

        return root