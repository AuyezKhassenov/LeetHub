class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        diff = (sum(aliceSizes) - sum(bobSizes)) / 2
        a = set(aliceSizes)
        for num2 in set(bobSizes):
            if num2 + diff in a:
                return [num2 + diff, num2]
        
        