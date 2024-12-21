class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        flip = False
        for num in nums:
            if num == 0:
                if flip:
                    continue
                else:
                    ans += 1
                    flip = True
            else:
                if flip:
                    ans += 1
                    flip = False
                else:
                    continue
        return ans