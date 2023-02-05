class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        heap = []
        for gift in gifts: heappush(heap, -gift)
        
        g = -heappop(heap)
        
        for _ in range(k):
            g = -heappushpop(heap, -isqrt(g))
            
        return g - sum(heap)