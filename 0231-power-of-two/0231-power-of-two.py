class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return str(bin(n).split('b')[1]).count('1') == 1 if n > 0 else False
            
        