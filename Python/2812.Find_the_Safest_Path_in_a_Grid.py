from typing import List
from collections import deque
import heapq

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        # get the dimensions of the grid
        row_length, col_length = len(grid), len(grid[0])
        
        # if the start or end points are unsafe, return 0
        if grid[0][0] == 1 or grid[row_length - 1][col_length - 1] == 1:
            return 0
        
        # initialize a 2D array to store the safeness factor of each cell
        safeness = [[-1] * col_length for _ in range(row_length)]
        # initialize a deque to perform BFS
        queue = deque([])
        
        # mark the unsafe cells as safe (safeness factor = 0) and add them to the queue
        for r in range(row_length):
            for c in range(col_length):
                if grid[r][c] == 1:
                    safeness[r][c] = 0
                    queue.append((0, r, c))
                    
        # define the four directions (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # perform BFS to calculate the safeness factor of each cell
        while queue:
            distance, r, c = queue.popleft()
            for dr, dc in directions:
                new_row, new_col = r + dr, c + dc
                # check if the new cell is within the grid and is unvisited
                if (
                    0 <= new_row < row_length
                    and 0 <= new_col < col_length
                    and safeness[new_row][new_col] == -1
                ):
                    # update the safeness factor of the new cell and add it to the queue
                    safeness[new_row][new_col] = distance + 1
                    queue.append((distance + 1, new_row, new_col))
        
        # initialize a min-heap to find the maximum safeness factor
        heap = [
            (-safeness[row_length - 1][col_length - 1], row_length - 1, col_length - 1)
        ]
        # initialize a set to keep track of visited cells
        seen = set([(row_length - 1, col_length - 1)])
        
        # use Dijkstra's algorithm with a min-heap to find the maximum safeness factor
        while heap:
            distance, r, c = heapq.heappop(heap)
            # if we reach the start cell, return the maximum safeness factor
            if (r, c) == (0, 0):
                return -distance
            
            # explore neighboring cells
            for dr, dc in directions:
                new_row, new_col = r + dr, c + dc
                # check if the new cell is within the grid and is unvisited
                if (
                    0 <= new_row < row_length
                    and 0 <= new_col < col_length
                    and (new_row, new_col) not in seen
                ):
                    # calculate the safeness factor of the new cell and add it to the heap
                    safe = max(distance, -safeness[new_row][new_col])
                    heapq.heappush(heap, (safe, new_row, new_col))
                    seen.add((new_row, new_col))
        
        # if no path is found, return -1
        return -1

if __name__ == '__main__':
    s = Solution()
    print(s.maximumSafenessFactor([[1,0,0],[0,0,0],[0,0,1]]))
    print(s.maximumSafenessFactor([[0,0,1],[0,0,0],[0,0,0]]))
    print(s.maximumSafenessFactor([[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]))