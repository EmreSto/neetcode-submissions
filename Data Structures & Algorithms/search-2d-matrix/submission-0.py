class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for index, row in enumerate(matrix):
            if target <= row[-1]:
                left = 0
                right = len(row)-1
                while left <= right:
                    mid = (left + right) // 2
                    if row[mid] > target:
                        right = mid - 1 
                    elif row[mid] < target:
                        left = mid + 1 
                    elif row[mid] == target:
                        return True

        return False   


        