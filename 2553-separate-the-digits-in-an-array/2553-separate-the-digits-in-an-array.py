class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            res += [int(n) for n in str(num)]
        return res
        