class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        duplicate = set()
        for i in range(n-2):
        
            
            first = nums[i]
           # if i > 0 and first == prev:
           #     continue
            l = i + 1
            r = n - 1
            while l < r:
                left, right = nums[l], nums[r]
                if left + right > -first:
                    r -= 1
                elif left + right < - first:
                    l += 1
                else:
                    if (first, left, right) not in duplicate:
                        res.append([first, left, right])
                        duplicate.add((first, left, right))
                    r -= 1
                    l += 1
                    
            #prev = first
        return res
            