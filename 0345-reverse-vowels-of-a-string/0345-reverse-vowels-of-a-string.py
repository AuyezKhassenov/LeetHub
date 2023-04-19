class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a','e','i','o','u', 'A','E','I','O','U'}
        temp = []
        for char in s:
            if char in vowels:
                temp.append(char)
        if not temp:
            return s
        s = [char for char in s]
        for i, char in enumerate(s):
            if char in vowels:
                s[i] = temp.pop()
        return "".join(s)
                
        