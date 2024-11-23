class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        return all(v % 2 == 0 for k, v in Counter(nums).items())