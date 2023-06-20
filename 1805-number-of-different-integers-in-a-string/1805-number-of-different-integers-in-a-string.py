class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        res = set()
        num = ''
        for i, char in enumerate(word):
            if char.isnumeric():
                num += char
            else:
                if num != '':
                    res.add(int(num))
                    num = ''
        if num != '':
            res.add(int(num))
        return len(res)
        