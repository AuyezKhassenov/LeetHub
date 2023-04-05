class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.res = 0
        
        def bt(i, path):
            if i == len(nums):
                self.res += self.xor(path[::])
                return
            
           
            bt(i+1, path + [nums[i]])
            bt(i+1, path)
            
        bt(0, [])
        return self.res      
          
        
    def xor(self, arr):
        xor_arr = 0
        for num in arr:
            xor_arr = xor_arr ^ num
        return xor_arr
        
        
        