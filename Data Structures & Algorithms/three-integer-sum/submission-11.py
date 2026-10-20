class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        target = 0
        sort_nums = sorted(nums)
        for i in range(len(sort_nums)):
            target = -sort_nums[i]
            if i > 0 and sort_nums[i] == sort_nums[i-1]:
                continue
            left = i + 1
            right = len(sort_nums) -1 
            while left < right:
                if sort_nums[left] + sort_nums[right] < target:
                    left = left + 1
                elif sort_nums[left] + sort_nums[right] > target:
                    right = right - 1
                elif sort_nums[left] + sort_nums[right] == target:
                    result.append([sort_nums[left],sort_nums[right],sort_nums[i]])
                    left = left + 1
                    right = right -1
                    while left < right and sort_nums[left] == sort_nums[left-1]:
                        left = left + 1 
        return result
            
        