class Solution:
    def minFallingPathSum(self, grid: list[list[int]]) -> int:
        # Get the dimensions of the grid
        row_length, col_length = len(grid), len(grid[0])
        
        # iterate over each row starting from the second row
        for r in range(1, row_length):
            # iterate over each column in the current row
            for c in range(col_length):
                # store the value of the element in the previous row and same column
                temp = grid[r - 1][c]
                # set the value of the element in the previous row and same column to infinity
                grid[r - 1][c] = float('inf')
                # update the current element by adding the minimum value from the previous row
                grid[r][c] += min(grid[r - 1])
                # restore the original value of the element in the previous row and same column
                grid[r - 1][c] = temp
        
        # return the minimum value from the last row of the grid
        return min(grid[len(grid) - 1])

if __name__ == '__main__':
    s = Solution()
    print(s.minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]))
    print(s.minFallingPathSum([[7]]))