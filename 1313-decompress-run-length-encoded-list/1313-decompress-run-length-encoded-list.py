class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)//2):
            res += nums[2*i]*[nums[2*i + 1]]
        return res
        