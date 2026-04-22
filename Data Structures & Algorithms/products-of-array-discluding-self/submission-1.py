class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        somet = len(nums)
        output = [1] * somet 
        prefix = 1
        for i in range(somet):
            output[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(somet-1,-1,-1):
            output[i] *= postfix
            postfix *= nums[i]
        return output

