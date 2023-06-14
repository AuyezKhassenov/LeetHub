class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda k: -k[1])
        res = 0
        for box, unit in boxTypes:
            if truckSize >= box:
                res += unit*box
                truckSize -= box
            else:
                res += unit*truckSize
                break
        return res