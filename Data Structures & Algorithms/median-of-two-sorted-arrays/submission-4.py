class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            temp = nums1
            nums1 = nums2
            nums2 = temp 
        total = len(nums1) + len(nums2)
        half = (total + 1) // 2
        L = 0
        R = len(nums1)
        result = 0

        while L <= R:
            i = (L+R) // 2
            j = half -i
            if i == 0:
                A = float("-inf")
            else:
                A = nums1[i-1]
            if i == len(nums1):
                B = float("inf")
            else:
                B = nums1[i]
            if j == 0:
                C = float("-inf")
            else:
                C = nums2[j-1]
            if j == len(nums2):
                D = float("inf")
            else:
                D = nums2[j]
            if A > D:
                R = i -1
            elif C > B:
                L = i + 1
            else:
                if total % 2 == 0:
                    result = (max(A,C) + min(B,D)) / 2
                    break
                else:
                    result = max(A,C)
                    break
        return result
            
            

