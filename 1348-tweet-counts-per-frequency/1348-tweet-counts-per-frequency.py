class TweetCounts:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.freqs = {'minute':60,
                      'hour':3600,
                      'day': 86400}
        
    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets[tweetName].append(time)
        

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        time = self.freqs[freq]
        res = [0] * (((endTime - startTime) // time) + 1)
        for i in self.tweets[tweetName]:
            if startTime <= i <= endTime: res[(i - startTime) // time] += 1
        
        
                
            
        return res
                
            
            
            
            
            
        


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)