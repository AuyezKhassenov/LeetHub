class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(i, cur_sum):
            if i == len(nums) and cur_sum == target:
                return 1
            if i >= len(nums):
                return 0
            if (i, cur_sum) in memo:
                return memo[(i, cur_sum)]
            
            left = dfs(i+1, cur_sum + nums[i])
            right = dfs(i+1, cur_sum - nums[i])
            memo[(i, cur_sum)] = left+right
            return left + right
        return dfs(0, 0)