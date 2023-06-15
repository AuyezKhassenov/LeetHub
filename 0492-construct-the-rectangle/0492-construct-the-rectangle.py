import math
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        L = math.floor(sqrt(area))
        for w in range(L, area+1):
            if not area%w:
                return [max(w, area//w), min(w, area//w)]
        