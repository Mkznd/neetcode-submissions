class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = [i for i in s.lower() if i.isalpha() or i.isdigit()]
        print(l)
        return l == l[::-1]