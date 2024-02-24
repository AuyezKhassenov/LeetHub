class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        ans = 10e6
        cur = 0
        for r, num in enumerate(nums):
            cur += num

            while cur >= target:
                ans = min(ans, r - l + 1)
                cur -= nums[l]


                l += 1
        return ans if ans < 10e6 else 0
                
            