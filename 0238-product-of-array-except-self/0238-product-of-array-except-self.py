class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cnt_zero = nums.count(0)
        if cnt_zero >= 2:
            return [0 for num in nums]
        elif cnt_zero == 1:
            
            return [0 if num!= 0 else reduce((lambda x,y: x*y), [num if num != 0 else 1 for num in nums]) for num in nums]
        else:
            mult = reduce((lambda x,y: x*y), [num for num in nums])
            return [mult//num for num in nums]
        