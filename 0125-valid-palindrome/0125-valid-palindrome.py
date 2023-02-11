class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_ = ''.join([char.lower() for char in s if char.isalnum()])
        print(str_)
        return str_ == str_[::-1]
        