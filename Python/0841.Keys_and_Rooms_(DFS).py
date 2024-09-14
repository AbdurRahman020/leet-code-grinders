from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # initialize a list to keep track of visited rooms, start with all rooms 
        # marked as unvisited (False)
        visited = [False] * len(rooms)
        
        # mark the first room (room 0) as visited
        visited[0] = True
        
        # define a helper function to perform Depth-First Search (DFS)
        def dfs(room):
            # iterate over all rooms accessible from the current room
            for i in rooms[room]:
                # if the neighboring room has not been visited yet
                if not visited[i]:
                    # mark this room as visited
                    visited[i] = True
                    # recursively visit this room's neighbors
                    dfs(i)
        
        # start DFS from room 0
        dfs(0)
        
        # check if all rooms have been visited, return True if all rooms are visited, otherwise False
        return all(visited)

if __name__ == '__main__':
    s = Solution()
    print(s.canVisitAllRooms([[1],[2],[3],[]]))
    print(s.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))