class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        pos_prev = -k - 1
        
        for i, num in enumerate(nums):
            
            if num == 1:
                dist = i - pos_prev - 1
                pos_prev = i
                
                if dist < k:
                    return False
                
        return True
            
                
                    
        