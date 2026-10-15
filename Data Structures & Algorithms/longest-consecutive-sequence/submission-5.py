class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        in_result = 1
        result = 1
        my_set = set(nums)
        if len(my_set) == 0:
            return 0
        for num in my_set:
            if num-1 not in my_set:
                start_number = num
                while start_number+1 in my_set:
                    in_result +=1
                    if in_result > result:
                        result = in_result
                    start_number += 1
                in_result = 1
        return result


        