class Solution:
    def modifyString(self, s: str) -> str:
        s = [char for char in s]
        n = len(s) - 1
        if n == 0: return 'a'
        start, finish = ord('a'), ord('z')
        for i, char in enumerate(s):
            if char == '?':
                if i == 0:
                    for j in range(start, finish+1):
                        if s[i+1] != chr(j):
                            s[i] = chr(j)
                            break
                elif i == n:
                    for j in range(start, finish+1):
                        if s[i-1] != chr(j):
                            s[i] = chr(j)
                            break
                else:
                    for j in range(start, finish+1):
                        if s[i-1] != chr(j) and s[i+1] != chr(j):
                            s[i] = chr(j)
                            break
        return ''.join(s)
            
        