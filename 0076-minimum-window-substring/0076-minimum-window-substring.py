class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #s = "babb"
        #t = "baba"
        if len(s) < len(t):
            return ''
        cnt_t = Counter(t)
        min_res = len(s)
        res = ''

     
        for i, char in enumerate(s):
            if i == len(s)-1 and char not in cnt_t:
                return ''
            if char in cnt_t:
                l = i
                break
        
        match = 0      
        for r in range(l, len(s)):
            if s[r] in cnt_t:
                if cnt_t[s[r]] == 1 : match += 1
                cnt_t[s[r]] -= 1
                
            if match == len(cnt_t):
                #print(s[l:r+1])
                while cnt_t[s[l]] < 0 or s[l] not in cnt_t:
                    if s[l] in cnt_t:
                        cnt_t[s[l]] += 1
                    l += 1
                    
                if r-l+1 <= min_res:
                    res = s[l:r+1]
                    min_res = r - l + 1
                    
                #if cnt_t[s[l]] == 0: match -= 1
                #cnt_t[s[l]] += 1
                '''
                for i in range(l+1, r+1):
                    l = i
                    if s[l] in cnt_t:
                        #cnt_t[s[l]] = 1
                        break
                '''
        return res