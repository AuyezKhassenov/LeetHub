class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for key, val in Counter(nums).items():
            if val != 1:
                return key
        