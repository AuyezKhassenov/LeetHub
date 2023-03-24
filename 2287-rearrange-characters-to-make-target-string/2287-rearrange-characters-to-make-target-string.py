from collections import Counter
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        return min([s.count(key)//val for key, val in Counter(target).items()])
        
        