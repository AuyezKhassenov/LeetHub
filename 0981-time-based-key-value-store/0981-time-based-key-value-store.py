class TimeMap:

    def __init__(self):
        self.key_val = defaultdict()
        self.key_time = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_val[(key, timestamp)] = value
        self.key_time[key].append(timestamp)
        
    def get(self, key: str, timestamp: int) -> str:
        tmp = self.key_time[key]
        if len(tmp) == 0 or timestamp < tmp[0]:
            return ""
        l, r = 0, len(tmp) - 1
       
        
        while l <= r:
            m = (l+r) // 2                
            
            if tmp[m] < timestamp:
                l = m + 1
            elif tmp[m] > timestamp:
                r = m - 1
            else:
                return self.key_val[(key, tmp[m])]
        
        if timestamp > tmp[m]:
            ind = min(len(tmp)-1,m+1)
        else:
            ind = max(0, m-1)
        return self.key_val[(key, tmp[ind])] 
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)