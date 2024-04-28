class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        
        row_length, col_length = len(grid), len(grid[0])
        
        def dfs(r, c):
            if r < 0 or r >= row_length or c < 0 or c >= col_length or grid[r][c] != '1':
                return
            grid[r][c] = '0'
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        num_is_land = 0
        for i in range(row_length):
            for j in range(col_length):
                if grid[i][j] == '1':
                    num_is_land += 1
                    dfs(i,j)
        
        return num_is_land
    
if __name__ == '__main__':
    s = Solution()
    print(s.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))
    print(s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))