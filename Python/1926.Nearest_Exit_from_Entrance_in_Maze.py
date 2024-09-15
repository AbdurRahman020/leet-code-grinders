from typing import List
from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # directions for moving right, down, left, and up
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # get the dimensions of the maze
        m, n = len(maze), len(maze[0])
        
        # initialize a queue for BFS with the entrance and a distance of 0
        queue = deque([(entrance[0], entrance[1], 0)])
        
        # mark the entrance as visited
        maze[entrance[0]][entrance[1]] = '+'
        
        # perform BFS
        while queue:
            # dequeue the current position and distance
            x, y, dist = queue.popleft()
            
            # explore all 4 possible directions (right, down, left, up)
            for dx, dy in dirs:
                # calculate new position
                nx, ny = x + dx, y + dy
                # check if the new position is within bounds and is not visited
                if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == '.':
                    # check if the new position is on the boundary of the maze (an exit)
                    if nx == 0 or ny == 0 or nx == m - 1 or ny == n - 1:
                        # return the distance to the exit
                        return dist + 1
                    
                    # mark the new position as visited
                    maze[nx][ny] = '+'
                    # add the new position and updated distance to the queue
                    queue.append((nx, ny, dist + 1))
        
        # if no exit is found, return -1
        return -1

if __name__ == '__main__':
    s = Solution()
    print(s.nearestExit([["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], [1,2]))
    print(s.nearestExit([["+","+","+"],[".",".","."],["+","+","+"]], [1,0]))
    print(s.nearestExit([[".","+"]], [0,0]))