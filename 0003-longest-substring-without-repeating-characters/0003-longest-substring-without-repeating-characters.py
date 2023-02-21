class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) < 2: return len(s)
        res = 0
        l,r = 0,1
        used = {s[l]:l}
        while r < len(s):
      
            if not(s[r] not in used or used[s[r]] < l):
                res = max(res, r-l)
                l = used[s[r]] + 1
                
            used[s[r]] = r
            r += 1
            if r == len(s):
                res = max(res, r-l)

        return res
            
            
            
         
       
            
            
     
            
