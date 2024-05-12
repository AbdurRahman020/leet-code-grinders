class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        # get the size of the grid
        n = len(grid)
        # initialize the result grid with appropriate dimensions
        result = [[0]*(n-2) for _ in range(n-2)]
        
        # iterate through the grid, excluding the last 2 rows and columns
        for r in range(n-2):
            for c in range(n-2):
                # find the maximum value in the 3x3 subgrid starting at (r,c)
                result[r][c] = max(grid[i][j] for i in range(r, r+3) for j in range(c, c+3))
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.largestLocal([[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]))
    print(s.largestLocal([[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]))