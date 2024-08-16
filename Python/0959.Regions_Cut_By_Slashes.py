from typing import List

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        # define a depth-first search (DFS) function to explore connected regions
        def dfs(x, y):
            # check if the current position is out of bounds or already visited (1)
            if x < 0 or y < 0 or x >= len(grid_expanded) or y >= len(grid_expanded) or grid_expanded[x][y] != 0:
                # if out of bounds or already visited, return 0
                return 0
            
            # mark the current cell as visited by setting it to 1
            grid_expanded[x][y] = 1
            
            # recursively visit all adjacent cells (up, down, left, right) and sum up the regions
            return 1 + dfs(x - 1, y) + dfs(x + 1, y) + dfs(x, y - 1) + dfs(x, y + 1)
        
        # get the size of the input grid
        grid_size = len(grid)
        # initialize the count of regions
        region_count = 0
        
        # create an expanded grid to accommodate the slashes and backslashes,
        # each cell in the original grid is expanded into a 3x3 block in the new grid
        grid_expanded = [[0]*(grid_size*3) for _ in range(grid_size*3)]
        
        # fill the expanded grid based on the slashes and backslashes in the input grid
        for r in range(grid_size):
            for c in range(grid_size):
                if grid[r][c] == '/':
                    # for '/' slash, mark the relevant cells in the expanded grid
                    grid_expanded[r*3][c*3 + 2] = grid_expanded[r*3 + 1][c*3 + 1] = grid_expanded[r*3 + 2][c*3] = 1
                elif grid[r][c] == '\\':
                    # for '\\' backslash, mark the relevant cells in the expanded grid
                    grid_expanded[r*3][c*3] = grid_expanded[r*3 + 1][c*3 + 1] = grid_expanded[r*3 + 2][c*3 + 2] = 1
        
        # traverse each cell in the expanded grid and use DFS to count the number of regions
        for r in range(grid_size * 3):
            for c in range(grid_size * 3):
                # if a new region is found (dfs returns more than 0)
                if dfs(r, c) > 0:
                    # increment the region count
                    region_count += 1
        
        # return the total number of regions
        return region_count

if __name__ == '__main__':
    s = Solution()
    print(s.regionsBySlashes(["/\\","\\/"]))
    print(s.regionsBySlashes([" /","/ "]))
    print(s.regionsBySlashes([" /","  "]))