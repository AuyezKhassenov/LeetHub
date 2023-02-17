class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0
        for num in nums_set:
            if num - 1 in nums_set:
                continue
            else:
                length = 1
                while num + length in nums_set:
                    length += 1

                res = max(res, length)
            
        return res
        