class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_nums = sum(num for num in range(n+1))
        return sum_nums - sum(nums)