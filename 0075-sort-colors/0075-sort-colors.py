class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = Counter(nums)
        for i in range(len(nums)):
            if i < cnt[0]:
                nums[i] = 0
            elif i < cnt[0] + cnt[1]:
                nums[i] = 1
            else:
                nums[i] = 2