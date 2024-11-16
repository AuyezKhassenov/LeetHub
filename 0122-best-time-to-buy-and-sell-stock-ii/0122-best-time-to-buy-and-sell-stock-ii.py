class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_max = prices[-1]
        ans = 0
        
        for i in range(len(prices)-2, -1, -1):
            if prices[i] < cur_max:
                ans += cur_max - prices[i]
            cur_max = prices[i]
        return ans
