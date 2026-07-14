from collections import defaultdict

def count_elements(nums: list[int]) -> dict[int, list]:
    counts = defaultdict(lambda: 0)
    c_reverse = defaultdict(lambda: [])
    for i in nums:
        counts[i]+=1
    for key, val in counts.items():
        c_reverse[val].append(key)
    return c_reverse

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = count_elements(nums)
        ans = []
        print(dict(c))
        for i in range(len(nums), 0, -1):
            if i in c:
                ans.extend(c[i])
        return ans[:k]