class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                res = max(res, (nums[i]-1) * (nums[j]-1))
        return res