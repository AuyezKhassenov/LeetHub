class RecentCounter:

    def __init__(self):
        self.count = 0
        self.pings = deque([])

    def ping(self, t: int) -> int:
        self.pings.append(t)
        self.count += 1
        while True:
            if self.pings[0] < self.pings[-1]-3000:
                self.pings.popleft()
                self.count -= 1
            else:
                break
        return self.count
            
            


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)