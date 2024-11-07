class Solution:
    def clearDigits(self, s: str) -> str:
        marked = set()
        ans = []
        char_indices = []
        for i, char in enumerate(s):
            if char.isnumeric():
                if char_indices:
                    marked.add(char_indices.pop())
            else:
                char_indices.append(i)
                
        for i, char in enumerate(s):
            if not char.isnumeric() and not i in marked:
                ans.append(char)
        
        return "".join(ans)
        