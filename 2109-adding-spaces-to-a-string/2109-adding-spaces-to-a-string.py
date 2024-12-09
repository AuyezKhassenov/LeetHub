class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = []
        spaces_i = 0
        max_spaces_i = len(spaces)
        for i, char in enumerate(s):
            if spaces_i < max_spaces_i and i == spaces[spaces_i]:
                ans.append(' ')
                spaces_i += 1
            
            ans.append(char)
        
        return "".join(ans)