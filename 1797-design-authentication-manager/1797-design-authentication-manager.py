class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.auth_man = defaultdict(int)
        self.time = timeToLive
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.auth_man[tokenId] = currentTime
               
        

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.auth_man:
            if self.auth_man[tokenId] > currentTime - self.time:
                self.auth_man[tokenId] = currentTime
        

    def countUnexpiredTokens(self, currentTime: int) -> int:
        res = 0
        for val in self.auth_man.values():
            if val > currentTime - self.time:
                res += 1
        return res
            
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)