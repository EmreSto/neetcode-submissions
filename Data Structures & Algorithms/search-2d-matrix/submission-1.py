class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat_list = []
        for row in matrix:
            for value in row:
                flat_list.append(value)
        L=0
        R= len(flat_list)-1
        while L <= R:
            mid = (L+R) // 2
            if flat_list[mid] == target:
                return True
            elif flat_list[mid] < target:
                L = mid + 1
            elif flat_list[mid] > target:
                R = mid - 1 
        return False


        