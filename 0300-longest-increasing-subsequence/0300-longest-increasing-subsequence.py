class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums)-2, -1, -1):
            cur_max = 0
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    cur_max = max(cur_max, dp[j])
            if cur_max:
                dp[i] = cur_max + 1
        
        return max(dp)
        