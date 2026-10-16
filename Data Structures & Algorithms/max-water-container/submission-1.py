class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_so_far = 0
        max_area = 0
        left = 0
        right = len(heights)-1
        while left < right:
            max_so_far = (right-left) * min(heights[left],heights[right])
            if heights[left] < heights[right]:
                left = left + 1
            else:
                right = right - 1
            if max_so_far > max_area:
                max_area = max_so_far
        return max_area
        