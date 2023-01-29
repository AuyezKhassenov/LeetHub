class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        curr = 0
        res = 1
        for d in s:
            if int(d) > k:
                return -1
            curr = curr * 10 + int(d)
            if curr > k:
                res += 1
                curr = int(d)
        return res
            
                




                
            
            
            
        