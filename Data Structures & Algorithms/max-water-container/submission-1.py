class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxArea = (r - l) * min(heights[l], heights[r])
        while l < r:
            left = heights[l]
            right = heights[r]
            area = (r - l) * min(left, right)
            if (area > maxArea):
                maxArea = area
            if left < right:
                l += 1
            else:
                r -= 1
        return maxArea