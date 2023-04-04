class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for a in range(1, n):
            b = n - a
            if str(a).count('0') == 0 and str(b).count('0') == 0:
                return [a,b]
        