class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        if right == left:
            if nums[0] == target:
                return 0
        while left < right:
            mid = (left + right) // 2
            if right - left == 1:
                if target == nums[left]: return left
                elif target == nums[right]: return right
                else: return -1
            if target > nums[mid]:
                left = mid
            elif target < nums[mid]:
                right = mid
            else:
                return mid
            
        return -1
        