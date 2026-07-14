class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliments = {}
        for ind, i in enumerate(nums):
            if i in compliments:
                return [compliments[i], ind]
            compliments[target-i] = ind