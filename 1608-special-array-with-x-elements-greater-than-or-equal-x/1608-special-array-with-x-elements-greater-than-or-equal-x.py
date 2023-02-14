class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        for i in range(1, len(nums)+1):
            
            cnt = 0
            for num in nums:
                if num >= i:
                    cnt += 1
                else:
                    break
            if cnt == i:
                return i
        return -1
                    
            
        