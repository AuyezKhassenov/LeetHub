# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q_next = deque()
        res = []
        tmp = []
        if root:
            q.append(root)
        while q:
            node = q.popleft()
            tmp.append(node.val)
            
            if node.left:
                q_next.append(node.left)
            if node.right:
                q_next.append(node.right)
            if not q:
                res.append(tmp)
                tmp = []
                q = q_next
                q_next = deque()
        return res
                
            
                
                
        
        