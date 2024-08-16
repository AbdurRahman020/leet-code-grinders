from typing import List

class Solution:
    def numIslands(self, grid: List[List[int]]) -> int:
        # define a depth-first search (DFS) function to explore all connected land (1s)
        def dfs(x, y):
            # check if the current position is out of bounds or is water (0) or already visited
            if x < 0 or y < 0 or x >= row_length or y >= col_length or grid[x][y] != 1:
                return
            
            # mark the current land cell as visited by setting it to 0
            grid[x][y] = 0
            
            # recursively visit all adjacent cells (up, left, down, right)
            dfs(x-1, y)  # Visit cell above
            dfs(x, y-1)  # Visit cell to the left
            dfs(x+1, y)  # Visit cell below
            dfs(x, y+1)  # Visit cell to the right
        
        # initialize the count of islands
        num_of_island = 0
        
        # number of rows in the grid
        row_length = len(grid)
        # number of columns in the grid
        col_length = len(grid[0])
        
        # traverse each cell in the grid
        for r in range(row_length):
            for c in range(col_length):
                # if the current cell is land (1), it signifies a new island
                if grid[r][c] == 1:
                    # increment the island count
                    num_of_island += 1
                    # perform DFS to mark the entire island as visited
                    dfs(r, c)
        
        # return the total number of islands found
        return num_of_island
    
    def minDays(self, grid: List[List[int]]) -> int:
        # number of rows in the grid
        row_length = len(grid)
        # number of columns in the grid
        col_length = len(grid[0])
        
        # create a copy of the grid to avoid modifying the original grid during DFS operations
        mat = [[grid[r][c] for c in range(col_length)] for r in range(row_length)]
        
        # calculate the number of islands in the initial grid
        islands = self.numIslands(mat)
        
        # if the initial grid does not contain exactly one island, return 0
        if islands != 1:
            return 0
        
        # try removing each land cell to see if it affects the island count
        for r in range(row_length):
            for c in range(col_length):
                # if the cell is land
                if grid[r][c] == 1:
                    # temporarily set it to water (0)
                    grid[r][c] = 0
                    
                    # create a new grid with the cell removed
                    newisland = [[grid[r][c] for c in range(col_length)] for r in range(row_length)]
                    
                    # check the number of islands in the modified grid
                    if self.numIslands(newisland) != 1:
                        # if removing this cell causes more than one island, return 1
                        return 1  
                    
                    # restore the cell to its original state
                    grid[r][c] = 1
        
        # if removing any single cell does not disconnect the island, return 2
        return 2

if __name__ == '__main__':
    s = Solution()
    print(s.minDays([[0,1,1,0],[0,1,1,0],[0,0,0,0]]))
    print(s.minDays([[1,1]]))