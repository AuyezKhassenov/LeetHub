class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even = odd = 0
        
        for i, b in enumerate(bin(n).split('b')[1][::-1]):
            if b == '1':
                if i%2:
                    odd += 1
                else:
                    even += 1
        return [even, odd]
        