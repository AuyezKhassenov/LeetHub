class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #s = 'dvdf'
        if len(s) < 2: return len(s)
        res = 0
        l,r = 0,1
        used = {s[l]:l}
        while r < len(s):
            print('r:',r)        
            if s[r] not in used or used[s[r]] < l:
                pass
            else:
                
                res = max(res, r-l)
                l = used[s[r]] + 1
            used[s[r]] = r
            r += 1
            if r == len(s):
                res = max(res, r-l)
            #print('l:',l)
            #print(res)
        return res
            
            
            
         
       
            
            
     
            
