class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        n = len(grid)

        row_map = {}
        for row in grid:
            key = tuple(row)          
            if key in row_map:
                row_map[key] += 1
            else:
                row_map[key] = 1

        
        for col in range(n):
            column = []
            for row in range(n):
                column.append(grid[row][col])  

            key = tuple(column)
            if key in row_map:
                count += row_map[key]   

        return count
