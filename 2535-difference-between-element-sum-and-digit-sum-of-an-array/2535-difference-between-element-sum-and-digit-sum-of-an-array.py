class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        return sum(nums) - sum(int(d) for num in nums for d in str(num))
        