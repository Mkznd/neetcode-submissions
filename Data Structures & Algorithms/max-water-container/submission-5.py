class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l , r = 0 , len(heights) - 1
        res = 0

        while l < r:
            minH = min(heights[l], heights[r])
            area = (r - l) * minH
            res = max(res, area)

            while l < r and heights[l] <= minH:
                l += 1
            while l < r and heights[r] <= minH:
                r -= 1
        
        return res
