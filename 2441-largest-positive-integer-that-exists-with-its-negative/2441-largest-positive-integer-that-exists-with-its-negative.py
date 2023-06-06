class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        res = -1
        used = set()
        for num in nums:
            if -num in used:
                res = max(res, abs(num))
            used.add(num)
        return res
        