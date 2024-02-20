class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)
        sum_ = size * (size + 1) // 2
        sum_nums = sum(nums)
        return sum_ - sum_nums
        