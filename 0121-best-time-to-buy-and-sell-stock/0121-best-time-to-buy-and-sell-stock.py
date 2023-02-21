class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_ = float('infinity')
        res = 0
        for price in prices:
            min_ = min(min_, price)
            res = max(res, price - min_)
        return res
            