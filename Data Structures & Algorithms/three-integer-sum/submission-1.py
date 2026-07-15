class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        print(nums)
        triplets = set()

        for i in range(len(nums)):
            left, right = 0, len(nums)-1
            while left < right:
                if left == i:
                    left += 1
                    continue
                if right == i:
                    right -= 1
                    continue

                l, r, cur = nums[left], nums[right], nums[i]
                if l + r + cur == 0:
                    triplets.add(tuple(sorted([l,r,cur])))
                    l+=1
                if l + r + cur > 0:
                    right -= 1
                else:
                    left += 1

        return [list(i) for i in triplets]