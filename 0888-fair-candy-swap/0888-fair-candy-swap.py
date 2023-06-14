class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        diff = (sum(aliceSizes) - sum(bobSizes)) / 2
        a = set(aliceSizes)
        for num1 in a:
            if num1 - diff in bobSizes:
                return [num1, num1-diff]
        
        