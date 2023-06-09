class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        res = 0
        tmp = 0
        n = len(nums)
        while i != n:
            if nums[i] == 1:
                tmp += 1
                if i == n-1:
                    res = max(res, tmp)
            else:
                res = max(res, tmp)
                tmp = 0
            i += 1
        return res
                