class Solution:
    def trap(self, height: list[int]) -> int:
        area = 0

        left = 0

        for i in range(len(height)):
            if i == 0 or i == len(height)-1:
                continue
            h = min(max(height[:i]), max(height[i+1:])) - height[i]
            h = h if h > 0 else 0
            area += h

        return area
