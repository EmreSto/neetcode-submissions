class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        output = [1] * length

        prefix = 1
        for i in range(length):
            output[i] = prefix
            prefix *= nums[i]
        psfix = 1
        for i in range(length -1, -1, -1):
            output[i] *= psfix
            psfix *= nums[i]
        return output
