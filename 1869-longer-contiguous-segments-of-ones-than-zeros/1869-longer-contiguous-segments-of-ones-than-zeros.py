class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        ones = zeroes = 0
        tmp_ones = tmp_zeroes = 0
        for num in s:
            if num == '0':
                tmp_zeroes += 1
                ones = max(ones, tmp_ones)
                tmp_ones = 0
            else:
                tmp_ones += 1
                zeroes = max(zeroes, tmp_zeroes)
                tmp_zeroes = 0
        ones, zeroes = max(ones, tmp_ones), max(zeroes, tmp_zeroes)
        return ones > zeroes
        
        