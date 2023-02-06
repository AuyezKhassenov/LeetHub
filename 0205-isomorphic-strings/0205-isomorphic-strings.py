class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict = defaultdict(int)
        s_order = defaultdict(int)
        j = 0
        for i, ch in enumerate(s):
            if ch not in s_order:
                s_order[ch] = j
                j += 1
            s_dict[i] = s_order[ch]
        t_dict = defaultdict(int)
        t_order = defaultdict(int)
        j = 0   
        for i, ch in enumerate(t):
            if ch not in t_order:
                t_order[ch] = j
                j += 1
            t_dict[i] = t_order[ch]
        
        return t_dict == s_dict
            
            
        