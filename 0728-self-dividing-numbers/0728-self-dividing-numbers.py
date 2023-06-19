class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for num in range(left, right+1):
            if all(digit != '0' and not num % int(digit) for digit in str(num)):
                res.append(num)
        return res