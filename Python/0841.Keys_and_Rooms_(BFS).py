from typing import List
from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # initialize a list to keep track of visited rooms, start with all rooms 
        # marked as unvisited (False)
        visited = [False] * len(rooms)
        
        # mark the first room (room 0) as visited
        visited[0] = True
        
        # initialize a queue for BFS (Breadth-First Search) with the first room
        queue = deque([0])
        
        # perform BFS to visit all reachable rooms
        while queue:
            # remove and return the leftmost room from the queue
            vertex = queue.popleft()
            
            # iterate over all rooms that can be accessed from the current room
            for i in rooms[vertex]:
                # if this room has not been visited yet
                if not visited[i]:
                    # mark this room as visited
                    visited[i] = True
                    # add this room to the queue to explore its neighbors later
                    queue.append(i)
        
        # check if all rooms have been visited, return True if all rooms are visited, otherwise False
        return all(visited)

if __name__ == '__main__':
    s = Solution()
    print(s.canVisitAllRooms([[1],[2],[3],[]]))
    print(s.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))