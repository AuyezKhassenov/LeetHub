class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        first, second = s[:n//2], s[n//2:]
        cnt_1 = cnt_2 = 0
        vowels ={'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        for u,v in zip(first,second):
            if u in vowels:
                cnt_1 += 1
            if v in vowels:
                cnt_2 += 1
            
        return cnt_1 == cnt_2