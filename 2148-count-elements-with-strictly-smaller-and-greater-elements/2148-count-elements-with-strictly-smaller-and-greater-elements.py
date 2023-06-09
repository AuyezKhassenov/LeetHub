class Solution:
    def countElements(self, nums: List[int]) -> int:
        max_num, min_num = max(nums), min(nums)
        res = 0
        for num in nums:
            if num > min_num and num < max_num:
                res += 1
        return res