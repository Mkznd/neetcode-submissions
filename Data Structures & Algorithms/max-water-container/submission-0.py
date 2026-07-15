class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_v = 0

        while l < r:
            cur_v = min(heights[l], heights[r]) * (r-l)
            max_v = max(cur_v, max_v)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return max_v
