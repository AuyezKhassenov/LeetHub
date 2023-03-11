import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        
        while l <= r:
            m = (l + r) // 2
            
            time = sum([math.ceil(pile/m) for pile in piles])
            if time <= h:
                r = m - 1
                res = min(res, m)
            else:
                l = m + 1
        return res
        
    


        