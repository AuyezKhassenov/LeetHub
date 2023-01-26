class Solution:
    #4
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cnt = defaultdict(list)
        for string in strs:
            cnt[tuple(sorted(string))].append(string)
        return cnt.values()
        
            
        