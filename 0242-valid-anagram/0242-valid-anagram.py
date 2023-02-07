class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_cnt, t_cnt = Counter(s), Counter(t)
        return s_cnt == t_cnt
        