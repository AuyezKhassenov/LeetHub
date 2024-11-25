class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        ans = 0
        
        def isPrime(n):
            for i in range(2, int(sqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True
        
        for i in range(len(nums)):
            num = nums[i][i]
            if isPrime(num):
                ans = max(ans, num)
            
            num = nums[i][-i-1]
            if isPrime(num):
                ans = max(ans, num)
        return ans if ans > 1 else 0
        
        
        