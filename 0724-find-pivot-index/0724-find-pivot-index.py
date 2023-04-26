class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums[1:])

        
        for i, num in enumerate(nums[:-1]):

            if left == right:
                return i
            left += num
            right -= nums[i+1]
        if left == right:
            return len(nums)-1
        return -1
        