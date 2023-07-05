class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            res = 0
            while num >= 10:
                res += num%10
                num //= 10
            num += res
        return num