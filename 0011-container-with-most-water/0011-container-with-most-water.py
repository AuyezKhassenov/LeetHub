class Solution:
    def maxArea(self, H: List[int]) -> int:
        l, r = 0, len(H)-1
        area = 0
        while l <= r:
            h_l, h_r = H[l], H[r]
            area = max(area, (r-l)*min(h_l, h_r))
            if h_l >= h_r:
                r -= 1
            else:
                l += 1
        return area