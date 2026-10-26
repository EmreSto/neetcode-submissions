class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        my_stack = []
        max_area = -1 
        for i in range(len(heights)):
            while len(my_stack) !=0 and heights[my_stack[-1]] > heights[i]:
                popped = my_stack.pop()
                height = heights[popped]
                right_bound = i
                if len(my_stack) == 0:
                    left_bound = -1
                else:
                    left_bound = my_stack[-1]
                width = right_bound - left_bound - 1
                area = height * width 
                if area > max_area:
                    max_area = area
            my_stack.append(i)
        while len(my_stack) !=0:
            popped = my_stack.pop()
            height = heights[popped]
            right_bound = len(heights)
            if len(my_stack) == 0:
                left_bound = -1
            else:
                left_bound = my_stack[-1]
            width = right_bound - left_bound - 1
            area = height * width 
            if area > max_area:
                max_area = area
        return max_area
        