class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt = Counter()
        cnt_s1 = Counter(s1)
        l = 0
        n = len(s1)
        for r in range(len(s2)):
            cnt[s2[r]] += 1
            if r - l == len(s1):
                cnt[s2[l]] -= 1
                l += 1
            if all(cnt.get(key, 0) >= val for key,val in cnt_s1.items()):
                return True
            
        return False
                
                
                
                
        