class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        for i in range(1, 10):
            if i in nums1 and i in nums2:
                return i
        num1, num2 = min(nums1), min(nums2)
        if num1 > num2:
            return num2*10 + num1
        elif num1 < num2:
            return num1*10 + num2