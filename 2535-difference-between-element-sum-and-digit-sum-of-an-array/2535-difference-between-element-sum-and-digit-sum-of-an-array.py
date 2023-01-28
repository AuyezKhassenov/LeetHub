class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            if num >= 10:
                res += num - sum([int(i) for i in str(num)])
        return res
        