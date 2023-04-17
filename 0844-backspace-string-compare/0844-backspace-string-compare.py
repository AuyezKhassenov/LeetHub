class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
    
        s_, t_ = [], []
        for i in s:
            if i == '#':
                if s_:
                    s_.pop()
            else: 
                s_.append(i)
        for v in t:     
            if v == '#':
                if t_:
                    t_.pop()
            else:
                t_.append(v)
     
        return s_ == t_