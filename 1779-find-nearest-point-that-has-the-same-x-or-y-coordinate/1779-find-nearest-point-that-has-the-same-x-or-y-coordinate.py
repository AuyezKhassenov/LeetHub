class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        res = [float('inf'), -1]
        for i, point in enumerate(points):
            if x == point[0] or y == point[1]:
                dist = abs(x - point[0]) + abs(y - point[1])
                if dist < res[0]:
                    res = [dist, i]
        return res[1]
                    
        