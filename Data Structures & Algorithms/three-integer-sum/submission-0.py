class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        mylist = sorted(nums)
        resultlist = []
        for i in range(len(mylist)):
            left = i +1
            right = len(mylist) - 1
            if i > 0 and mylist[i] == mylist[i-1]:
                continue
            while left < right:
                if mylist[i] + mylist[left] + mylist[right] > 0:
                    right = right - 1
                elif mylist[i] + mylist[left] + mylist[right] <0:
                    left = left + 1
                elif mylist[i] + mylist[left] + mylist[right] == 0:
                    resultlist.append([mylist[i],mylist[left],mylist[right]])
                    left = left +1
                    right = right -1
                    while left < right and mylist[left] == mylist[left-1]:
                        left = left +1 
            
        return resultlist
             