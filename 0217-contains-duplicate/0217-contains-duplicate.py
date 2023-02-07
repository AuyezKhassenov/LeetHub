class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return any(val > 1 for key,val in Counter(nums).items())
        