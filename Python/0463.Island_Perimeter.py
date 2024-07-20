from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # determine the dimensions of the grid
        row_length, col_length = len(grid), len(grid[0])
        # initialize perimeter counter
        perimeter = 0
        
        # depth-first search (DFS) function to explore the island
        def dfs(r, c):
            # base case: if out of grid bounds or encountered water (0), contribute to perimeter
            if r < 0 or r >= row_length or c < 0 or c >= col_length or grid[r][c] == 0:
                return 1
            
            # base case: if already visited (-1), do not contribute to perimeter
            if grid[r][c] == -1:
                return 0
            
            # mark the current cell as visited by setting it to -1
            grid[r][c] = -1 
            
            # explore in all four directions and accumulate perimeter counts
            perimeter = dfs(r+1, c)   # down
            perimeter += dfs(r-1, c)  # up
            perimeter += dfs(r, c+1)  # right
            perimeter += dfs(r, c-1)  # left
            
            return perimeter
        
        # iterate through each cell in the grid
        for i in range(row_length):
            for j in range(col_length):
                # if the cell represents land (1), start DFS to calculate its perimeter
                if grid[i][j] == 1:
                    perimeter += dfs(i,j)
        
        # return the total perimeter
        return perimeter 

if __name__ == '__main__':
    s = Solution()
    print(s.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
    print(s.islandPerimeter([[1]]))
    print(s.islandPerimeter([[1,0]]))