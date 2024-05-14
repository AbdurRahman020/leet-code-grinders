from typing import List

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        # get the dimensions of the grid
        row_length, col_length = len(grid), len(grid[0])
        # set to keep track of visited cells
        visited = set()
        
        # depth first search function to explore adjacent cells
        def dfs(r, c):
            # base cases for stopping the recursion
            if (
                r < 0
                or r >= row_length
                or c < 0
                or c >= col_length
                or (r, c) in visited
                or grid[r][c] == 0
            ):
                return 0
            
            # mark the current cell as visited
            visited.add((r, c))
            
            # explore adjacent cells recursively
            up = dfs(r+1, c)
            down = dfs(r-1, c)
            right = dfs(r, c+1)
            left = dfs(r, c-1)
            
            # unmark the current cell as visited (backtracking)
            visited.remove((r, c))
            
            # return the maximum amount of gold collectible from the current cell
            return grid[r][c] + max(up, down, right, left)
        
        # initialize the maximum gold collected as 0
        max_gold = 0
        # iterate through each cell in the grid
        for i in range(row_length):
            for j in range(col_length):
                # if the cell has gold and has not been visited yet
                if grid[i][j] and (i, j) not in visited:
                    # update the maximum gold collected by exploring from this cell
                    max_gold = max(max_gold, dfs(i, j))
        
        # return the maximum gold collected
        return max_gold

if __name__ == '__main__':
    s = Solution()
    print(s.getMaximumGold([[0,6,0],[5,8,7],[0,9,0]]))
    print(s.getMaximumGold([[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]))
    print(s.getMaximumGold([[1,0,7,0,0,0],[2,0,6,0,1,0],[3,5,6,7,4,2],[4,3,1,0,2,0],[3,0,5,0,20,0]]))