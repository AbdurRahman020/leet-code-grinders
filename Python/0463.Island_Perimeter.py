class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        row_length, col_length = len(grid), len(grid[0])
        perimeter = 0

        def dfs(r, c):
            if r < 0 or r >= row_length or c < 0 or c >= col_length or grid[r][c] == 0:
                return 1
            if grid[r][c] == -1:
                return 0
            
            grid[r][c] = -1 

            perimeter = dfs(r+1, c)
            perimeter += dfs(r-1, c)
            perimeter += dfs(r, c+1)
            perimeter += dfs(r, c-1)

            return perimeter
        
        for i in range(row_length):
            for j in range(col_length):
                if grid[i][j] == 1:
                    perimeter += dfs(i,j)
        
        return perimeter 

if __name__ == '__main__':
    s = Solution()
    print(s.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
    print(s.islandPerimeter([[1]]))
    print(s.islandPerimeter([[1,0]]))