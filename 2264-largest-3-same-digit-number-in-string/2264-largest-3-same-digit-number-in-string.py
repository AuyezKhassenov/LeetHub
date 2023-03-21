class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        res = ''
        l = 1
        prev = tmp = num[0]
        while l < len(num):
            cur = num[l]
            if cur == prev:
                tmp += cur
               
                if len(tmp) == 3:
                   
                    res = max(res, tmp)
                    tmp = ''
            else:
                tmp = cur
            l += 1
            prev = cur
            
        return res
            
            
        