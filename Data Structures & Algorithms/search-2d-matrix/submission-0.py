class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        low = 0
        high = m*n -1

        while low <= high:
            mid = (low + high) // 2
            #print(mid)
            num = matrix[mid//n][mid%n]
            #print(num)
            if num == target:
                return True
            elif num < target:
                low = mid + 1
            elif num > target:
                high = mid - 1
        return False
