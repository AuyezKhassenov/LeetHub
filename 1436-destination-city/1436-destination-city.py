class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        first = set()
        
        for one, two in paths:
            first.add(one)
        
        for one, two in paths:
            if two not in first:
                return two