class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            first = nums[i]
            l = i + 1
            r = n - 1
            while l < r:
                left, right = nums[l], nums[r]
                if left + right > -first:
                    r -= 1
                elif left + right < - first:
                    l += 1
                else:
                    res.append([first, left, right])
                    
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    
            
        return res
            