class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = [row[0] for row in matrix] + [matrix[-1][-1]]
        l, r = 0, len(matrix)
        if target < rows[0] or target > rows[-1]:
            return False
        while l <= r and r - l > 1:
            mid = (l + r)//2
            if rows[mid] < target:
                l = mid
            elif rows[mid] > target:
                r = mid
            else:
                return True
        if target > matrix[l][-1]:
            return False
        else:
            left, right = 0, len(matrix[l]) - 1
            while left <= right and right - left > 1:
                mid = (left + right) // 2
                if target > matrix[l][mid]:
                    left = mid
                elif target < matrix[l][mid]:
                    right = mid
                else:
                    return True
            
        return matrix[l][left] == target or matrix[l][right] == target
        