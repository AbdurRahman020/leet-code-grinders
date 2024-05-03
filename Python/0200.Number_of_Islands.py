class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        # base case: if grid is empty, there are no islands
        if not grid:
            return 0
        
        # the dimensions of the grid
        row_length, col_length = len(grid), len(grid[0])
        
        # depth first search (DFS) function to explore islands
        def dfs(r, c):
            # check if the current position is out of bounds or not part of an island
            if r < 0 or r >= row_length or c < 0 or c >= col_length or grid[r][c] != '1':
                return
            # mark the current position as visited (water)
            grid[r][c] = '0'
            # explore neighboring positions in all four directions
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        # initialize variable to count the number of islands
        num_is_land = 0
        # iterate through each cell in the grid
        for i in range(row_length):
            for j in range(col_length):
                # if the cell represents land and has not been visited yet
                if grid[i][j] == '1':
                    # increment the count of islands
                    num_is_land += 1
                    # explore the island using DFS to mark all connected land cells
                    dfs(i,j)
        
        # return the total number of islands
        return num_is_land
    
if __name__ == '__main__':
    s = Solution()
    print(s.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))
    print(s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))