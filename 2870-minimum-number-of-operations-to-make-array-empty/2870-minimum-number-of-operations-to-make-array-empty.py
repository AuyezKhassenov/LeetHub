class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = 0
        for val in cnt.values():
            if val == 1:
                return -1
            elif not val % 3:
                ans += val // 3
            elif val == 2:
                ans += 1
            else:
                ans += val // 3 + 1
        return ans
                