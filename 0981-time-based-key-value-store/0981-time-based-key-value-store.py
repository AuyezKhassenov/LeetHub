class TimeMap:

    def __init__(self):
        self.key_time = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_time[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        tmp = self.key_time[key]
        if len(tmp) == 0 or timestamp < tmp[0][1]:
            return ""
        
        l, r = 0, len(tmp) - 1
       
        while l <= r:
            m = (l+r) // 2                
            
            if tmp[m][1] < timestamp:
                l = m + 1
            elif tmp[m][1] > timestamp:
                r = m - 1
            else:
                return tmp[m][0]
        
        if timestamp > tmp[m][1]:
            ind = min(len(tmp)-1,m+1)
        else:
            ind = max(0, m-1)
        return tmp[ind][0]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)