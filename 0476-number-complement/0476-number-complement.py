class Solution:
    def findComplement(self, num: int) -> int:
        if num == 1:
            return 0
        b = bin(num)
        res = '0b'
        for i, char in enumerate(b[2:]):
            if i == 0:
                continue
            if char == '0':
                res += '1'
            else:
                res += '0'
        return int(res, 2)