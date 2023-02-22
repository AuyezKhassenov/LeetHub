class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt, match, w = Counter(s1), 0, len(s1)
        
        for i in range(len(s2)):
            if s2[i] in cnt:
                if not cnt[s2[i]]: match -= 1
                cnt[s2[i]] -= 1
                if not cnt[s2[i]]: match += 1
            
            if i >= w and s2[i-w] in cnt:
                if not cnt[s2[i-w]]: match -= 1
                cnt[s2[i-w]] += 1
                if not cnt[s2[i-w]]: match += 1
            
            if match == len(cnt):
                return True
        return False
                
                
                
                
        