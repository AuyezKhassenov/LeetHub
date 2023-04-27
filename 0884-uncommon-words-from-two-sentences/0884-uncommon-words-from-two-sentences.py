class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        cnt = Counter((s1 + ' ' + s2).split())
        return [word for word in cnt if cnt[word]==1]