class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        b, e = min(start, destination), max(start, destination)
        dist1 = sum(distance[b:e])
        dist2 = sum(distance) - dist1
        return min(dist1, dist2)