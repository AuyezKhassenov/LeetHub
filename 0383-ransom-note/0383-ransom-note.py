class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt1 = Counter(ransomNote)
        cnt2 = Counter(magazine)
        return all(cnt2.get(key, 0) - cnt1[key] >= 0 for key in cnt1.keys())