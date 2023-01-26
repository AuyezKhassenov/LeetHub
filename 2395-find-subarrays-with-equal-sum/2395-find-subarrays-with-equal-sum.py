class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        present = set()
        for i in range(len(nums) - 1):
            temp = nums[i] + nums[i+1]
            if temp not in present:
                present.add(temp)
            else:
                return True
        return False