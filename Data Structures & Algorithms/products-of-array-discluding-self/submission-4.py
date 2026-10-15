class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        right = [1] * len(nums)
        left = [1] * len(nums)
        for i in range(len(nums)):
            if i != 0:
                left[i] = left[i-1] * nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            right[i] = right[i+1] * nums[i+1]
        for i in range(len(nums)):
            answer = left[i] * right[i]
            output.append(answer)
        return output
         
                
        