class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid_index = (left + right) //2
            if nums[mid_index] > target:
                right = mid_index -1
            elif nums[mid_index] < target:
                left = mid_index +1
            elif nums[mid_index] == target:
                return mid_index
        return -1


            
