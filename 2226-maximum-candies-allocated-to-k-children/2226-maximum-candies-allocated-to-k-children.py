class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l, r = 1, max(candies)
        res = 0
        while l <= r:
            m = (l + r) // 2
            total = sum([c//m for c in candies])
            
            if total < k:
                r = m - 1
                
            else:
                l = m + 1
                res = max(res, m)
        return res
            
            