class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        result = 1
        
        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        return result
        
                
        