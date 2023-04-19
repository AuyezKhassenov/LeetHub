class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
        maxVal = -1
        for i, num in enumerate(nums):
            if num > maxVal:
                maxInd = i
                maxVal = num
        
        for num in nums:
            if num != maxVal and maxVal < 2 * num:
                return -1
        
        return maxInd
        