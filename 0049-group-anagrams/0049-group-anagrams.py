class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cnt = defaultdict(str)
        for string in strs:
            cnt[string] = ''.join(sorted(string)) 
        res = []
        strs.sort(key = lambda k:cnt[k])
        temp = [strs[0]]
        prev = strs[0]
        for string in strs[1:]:
            if cnt[string] == cnt[prev]:
                temp.append(string)
            else:
                res.append(temp)
                temp = [string]
                prev = string
                
        if temp == []:
            return res
        else:
            res.append(temp)
            return res
            
            
        