# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        val_to_idx = {val: idx for idx, val in enumerate(inorder)}
        
        def helper(inorder_start, inorder_end, preorder_start, preorder_end):
            if preorder_start > preorder_end:
                return None
            val = preorder[preorder_start]
            idx = val_to_idx[val]
            left_tree_size = idx - inorder_start
            root = TreeNode(val)
            root.left = helper(inorder_start, idx-1,
                               preorder_start+1, preorder_start + left_tree_size)
            root.right = helper(idx+1, inorder_end,
                               preorder_start + 1 + left_tree_size, preorder_end)
            
            
            return root
        return helper(0, len(inorder)-1, 0, len(preorder)-1)