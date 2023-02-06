class DetectSquares:

    def __init__(self):
        self.cnt = Counter()

    def add(self, point: List[int]) -> None:
        self.cnt[tuple(point)] += 1        

    def count(self, point: List[int]) -> int:
        res = 0
        x1,y1 = point
        for key,val in self.cnt.items():
            x3,y3 = key
            if abs(x1 - x3) == 0 or abs(x1-x3) != abs(y1-y3):
                continue
            res += val * self.cnt[(x1,y3)] * self.cnt[(x3,y1)]
            
        return res
                
            
                
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)