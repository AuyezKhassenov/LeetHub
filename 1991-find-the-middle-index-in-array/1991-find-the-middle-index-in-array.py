class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        sum1 = 0
        sum2 = sum(nums[1:])
        if sum1 == sum2: return 0

        for i in range(0, len(nums)-1):
            sum1 += nums[i]
            sum2 -= nums[i+1]
            if sum1 == sum2: return i+1

        return -1
            
        