from collections import defaultdict
class Solution:
    def count_in_word(self, s: str):
        count = [0] * 26
        for i in s:
            count[ord(i)-ord('a')] += 1
        return count

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_anagrams = defaultdict(lambda: [])
        for i in strs:
            str_anagrams[tuple(self.count_in_word(i))].append(i)
        return list(str_anagrams.values())