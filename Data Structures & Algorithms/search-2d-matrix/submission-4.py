class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L = 0
        R = len(matrix) -1
        while L <= R:
            mid = (L+R) // 2
            if matrix[mid][-1] < target:
                L = mid + 1
            elif matrix[mid][0] > target:
                R = mid - 1
            else:
                lo = 0
                hi = len(matrix[mid])-1
                while lo <= hi:
                    middo = (lo+hi) // 2
                    if matrix[mid][middo] == target:
                        return True
                    elif matrix[mid][middo] < target:
                        lo = middo + 1
                    elif matrix[mid][middo] > target:
                        hi = middo -1 
                return False
        return False
                
        