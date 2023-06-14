class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = empty = numBottles
        while empty >= numExchange:
            
            numBottles = empty//numExchange
            empty = empty - numBottles*(numExchange-1)
            res += numBottles
        
        return res