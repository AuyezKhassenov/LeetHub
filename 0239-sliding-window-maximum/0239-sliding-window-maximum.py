class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #nums = [9,10,9,-7,-4,-8,2,-6]
        #k = 7
        
        deque = []
        
        for i in range(k):
            if deque == []:
                deque.append(nums[i])
            else:
                while len(deque) > 0 and nums[i] > deque[-1]:
                    deque.pop()
                deque.append(nums[i])      
        
        res = [deque[0]]
        
        for r in range(k, len(nums)):
            while len(deque) > 0 and nums[r] > deque[-1]:
                deque.pop()
            
            if len(deque) and deque[0] == nums[r-k]:
                deque.pop(0)
            deque.append(nums[r])    
            res.append(deque[0])
            #print(deque)
                
        return res
            
        