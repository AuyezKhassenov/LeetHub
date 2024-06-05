# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        stack = []
        q = deque()
        q.append(root)
        stack.append(q)
        left_to_right = True
        while stack:
            q = stack.pop()
            tmp = []
            tmp_q = deque()
            while q:

                if not left_to_right:
                    node = q.pop()
                else:
                    node = q.popleft()
                if node:
                    tmp.append(node.val)

                    if left_to_right:
                        tmp_q.append(node.left)
                        tmp_q.append(node.right)
                    else:
                        tmp_q.appendleft(node.right)
                        tmp_q.appendleft(node.left)


            if tmp:
                ans.append(tmp)
                stack.append(tmp_q)

                left_to_right = not left_to_right

        return ans