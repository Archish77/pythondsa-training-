class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        n = len(matrix)

        result = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                result[j][n-1-i] = matrix[i][j]

        for i in range(n):
            for j in range(n):
                matrix[i][j] = result[i][j]