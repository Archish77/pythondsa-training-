class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
    
        row = [False] * m     # track which rows need to be zeroed
        col = [False] * n     # track which columns need to be zeroed
    
    # Pass 1: find all original zeroes
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True
    
    # Pass 2: apply the zeroes
        for i in range(m):
            for j in range(n):
                if row[i] or col[j]:
                    matrix[i][j] = 0
        