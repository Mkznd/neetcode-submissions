class Solution:
    def trap(self, height: list[int]) -> int:
        area = 0

        max_left = [-1] * len(height)
        max_right = [-1] * len(height)

        for i in range(len(height)):
            max_left[i] = max(max_left[i-1], height[i]) if i>0 else height[i]

        for i in range(len(height)-1, -1, -1):
            max_right[i] = max(max_right[i+1], height[i]) if i<len(height)-1 else height[i]

        for i in range(len(height)):
            if i == 0 or i == len(height)-1:
                continue
            h = min(max_left[i], max_right[i]) - height[i]
            h = h if h > 0 else 0
            area += h

        return area
