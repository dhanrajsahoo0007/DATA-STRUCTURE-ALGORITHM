class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for row in range(len(matrix[0])-1) :
            for column in range(len(matrix)-1):
                if target == matrix[row][column]:
                    return True
        return False





