from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if s == t:
            return True
            
        s_letters = defaultdict(lambda: 0)
        for i in s:
            s_letters[i] += 1
        t_letters = defaultdict(lambda: 0)
        for i in t:
            t_letters[i] += 1

        return s_letters == t_letters
