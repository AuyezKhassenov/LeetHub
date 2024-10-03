class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        allowed = len(candyType)/2
        n_types = len(list(set(candyType)))
        return int(min(allowed, n_types))