from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # check if the grid is empty
        if not grid:
            return -1
        
        # get the number of rows (m) and columns (n) in the grid
        m, n = len(grid), len(grid[0])
        
        # initialize a queue to perform BFS (Breadth-First Search)
        queue = deque()
        
        # count of fresh oranges
        fresh_oranges = 0
        
        # iterate over the grid to find all rotten oranges and count fresh oranges
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    # add the position of rotten oranges to the queue with initial time 0
                    queue.append((r, c, 0)) 
                elif grid[r][c] == 1:
                    # count the number of fresh oranges
                    fresh_oranges += 1
        
        # directions for moving up, down, left, right
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # variable to keep track of the maximum time taken to rot all oranges
        max_time = 0
        
        # process the BFS queue
        while queue:
            # get the position and time from the queue
            x, y, t = queue.popleft()
            
            # iterate over all possible directions (right, down, left, up)
            for dx, dy in directions:
                # calculate the new position
                nx, ny = x + dx, y + dy
                # if the new position is within bounds and contains a fresh orange
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    # rotten the orange
                    grid[nx][ny] = 2
                    # decrease the count of fresh oranges
                    fresh_oranges -= 1
                    # add the new position to the queue with incremented time
                    queue.append((nx, ny, t + 1))
                    # update the maximum time
                    max_time = max(max_time, t + 1)
        
        # if there are still fresh oranges left, return -1
        # otherwise, return the maximum time taken to rot all oranges
        return -1 if fresh_oranges > 0 else max_time

if __name__ == '__main__':
    s = Solution()
    print(s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
    print(s.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
    print(s.orangesRotting([[0,2]]))