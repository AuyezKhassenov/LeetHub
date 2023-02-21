#class Solution:# def lengthOfLongestSubstring(self, s: str) -> int:
'''
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
        
        used = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in used:
                used.remove(s[l])
                l += 1
            used.add(s[r])
            res = max(res, r - l + 1)
        return res
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        output = 0
        for r in range(len(s)):

            if s[r] not in seen:
                output = max(output,r-l+1)

            else:
                if seen[s[r]] < l:
                    output = max(output,r-l+1)
                else:
                    l = seen[s[r]] + 1
            seen[s[r]] = r
        return output        
            
         
       
            
            
     
            
