class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set(nums)
        counter = 0
        for num in nums:
            if num-1 not in myset:
                current =num
                length = 1
                while current + 1 in myset:
                    current += 1 
                    length +=1
                counter = max(counter, length)
        return counter

        
            



        