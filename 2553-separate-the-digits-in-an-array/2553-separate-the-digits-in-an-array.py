class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return [int(n) for num in nums for n in str(num)]