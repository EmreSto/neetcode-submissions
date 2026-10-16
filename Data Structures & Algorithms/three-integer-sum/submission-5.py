class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        target = 0
        sorted_nums = sorted(nums) 
        for i in range(len(sorted_nums)):
            target = -sorted_nums[i]
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
            left = i + 1
            right = len(sorted_nums)-1
            while left < right:
                if sorted_nums[left] + sorted_nums[right] < target:
                    left = left +1
                elif sorted_nums[left] + sorted_nums[right] > target:
                    right = right -1 
                elif sorted_nums[left] + sorted_nums[right] == target:
                    result.append([sorted_nums[left],sorted_nums[right],sorted_nums[i]])
                    left = left + 1
                    right = right - 1
                    while left < right and sorted_nums[left] == sorted_nums[left-1]:
                        left = left + 1
        return result
        