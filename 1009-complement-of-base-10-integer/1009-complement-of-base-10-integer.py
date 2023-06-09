class Solution:
    def bitwiseComplement(self, n: int) -> int:
        num = bin(n)
        res = '0b'
        for i, char in enumerate(num):
            if i > 1:
                if char == '1':
                    res += '0'
                else:
                    res += '1'
        return int(res, 2)