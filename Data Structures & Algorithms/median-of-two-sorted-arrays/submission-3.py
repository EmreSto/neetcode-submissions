class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for num in nums2:
            nums1.append(num)
        sort_nums = sorted(nums1)

        if len(sort_nums) % 2 == 0:
            L = (len(sort_nums) // 2) - 1
            R = ((len(sort_nums) // 2) + 1) -1
            median = (sort_nums[L] + sort_nums[R]) / 2
            return median
        else:
            odd_pos = ((len(sort_nums)+1) // 2) -1
            median = sort_nums[odd_pos]
            return median 

        