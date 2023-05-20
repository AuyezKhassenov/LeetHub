class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        correct = sorted(heights)
        res = 0
        for h, c in zip(heights, correct):
            if h != c:
                res += 1
        return res
