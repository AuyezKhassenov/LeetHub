class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            
            if nums[m] == target:
                return m
            
            
            if target > nums[m]:
                if target <= nums[r] or target > nums[m] > nums[l]:
                    l = m + 1
                else:
                    r = m - 1
                    
            elif target < nums[m]:
                if target >= nums[l] or target < nums[m] < nums[r]:
                    r = m - 1
                else:
                    l = m + 1
                
            '''
              
            if nums[l] <= target < nums[m]:
                r = m - 1
            else:
                l = m + 1
            
            '''
        return -1