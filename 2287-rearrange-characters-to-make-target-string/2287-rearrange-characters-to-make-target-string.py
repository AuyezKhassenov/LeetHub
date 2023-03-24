from collections import Counter
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        count_t = Counter(target)
        return min([s.count(key)//val for key, val in count_t.items()])
        
        