from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letters = defaultdict(lambda: 0)
        for i in s:
            s_letters[i] += 1
        t_letters = defaultdict(lambda: 0)
        for i in t:
            t_letters[i] += 1

        return s_letters == t_letters
