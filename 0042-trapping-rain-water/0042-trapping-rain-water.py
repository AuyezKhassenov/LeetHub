class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxLeft = maxRight = 0
        res = 0
        while l < r:
            maxLeft = max(maxLeft, height[l])
            maxRight = max(maxRight, height[r])
            
            if maxLeft <= maxRight:
                res += max(0, maxLeft - height[l])
                l += 1
            else: 
                res += max(0, maxRight - height[r])
                r -= 1
        return res
            
            
            
        