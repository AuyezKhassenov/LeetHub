class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        res = 0
        l,r = 0,len(nums)-1
        while l <= r:
            concat = int(str(nums[l]) + str(nums[r]))
            if l != r:
                res += concat
            else:
                res += nums[l]
            l, r = l+1, r-1
        return res
            
        