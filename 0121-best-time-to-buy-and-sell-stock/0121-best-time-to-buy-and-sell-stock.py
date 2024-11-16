class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_max = prices[-1]
        ans = 0
        
        for i in range(len(prices)-2, -1, -1):
            ans = max(cur_max - prices[i], ans)
            cur_max = max(cur_max, prices[i])
        return ans