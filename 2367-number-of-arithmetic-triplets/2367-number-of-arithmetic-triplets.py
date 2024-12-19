class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        ans = 0
        n = len(nums)
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n-1):
                if j > 1 and nums[j] == nums[j-1]:
                    continue
                for k in range(j+1, n):
                    if k > 2 and nums[k] == nums[k-1]:
                        continue
                    if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                        ans += 1
        return ans
                    