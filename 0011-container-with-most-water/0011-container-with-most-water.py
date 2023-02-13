class Solution:
    def maxArea(self, H: List[int]) -> int:
        l, r = 0, len(H) - 1
        res = 0
        while l < r:
            left, right = H[l], H[r]
            res = max(res, min(left, right)*(r-l))
            if left > right:
                r -= 1
            else:
                l += 1
        return res
        