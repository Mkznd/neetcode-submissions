class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_v = 0

        while l < r:
            minH = min(heights[l], heights[r])
            cur_v = minH * (r-l)
            max_v = max(cur_v, max_v)

            while l<r and heights[r] <= minH:
                r -= 1
            while l<r and heights[l] <= minH:
                l += 1
        
        return max_v
