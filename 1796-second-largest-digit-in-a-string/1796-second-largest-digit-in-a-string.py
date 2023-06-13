class Solution:
    def secondHighest(self, s: str) -> int:
        res = ['-1', '-1']
        for char in s:
            if char.isnumeric():
                if char > res[0]:
                    res = [char, res[0]]
                    continue
                elif char > res[1] and char != res[0]:
                    res = [res[0], char]
                    continue
        return int(res[1])
        