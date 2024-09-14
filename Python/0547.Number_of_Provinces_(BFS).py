from typing import List
from collections import deque

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # get the total number of cities (nodes in the graph)
        total_cities = len(isConnected)
        
        # special case: If there is only one city, it forms one province by itself
        if total_cities == 1:
            return 1
        
        # initialize a set to keep track of visited cities
        visited = set()
        
        # define a BFS function to explore all cities in the same province
        def bfs(city):
            # initialize the queue with the starting city for BFS
            queue = deque([city])
            # mark the starting city as visited
            visited.add(city)
            
            # perform BFS to visit all reachable cities
            while queue:
                # dequeue the current city
                curr_city = queue.popleft()
                
                # explore all neighboring cities
                for neighbor, is_connected in enumerate(isConnected[curr_city]):
                    # if there is a connection to the neighbor city and it hasn't been visited
                    if is_connected and (neighbor not in visited):
                        # mark the neighbor city as visited
                        visited.add(neighbor)
                        # enqueue the neighbor city for further exploration
                        queue.append(neighbor)
            
            return
        
        # initialize the count of provinces (connected components)
        province_count = 0
        
        # Iterate through each city
        for city in range(total_cities):
            # if the city has not been visited yet
            if city not in visited:
                # increment the province count
                province_count += 1
                # start BFS from this city to explore the entire province
                bfs(city)
        
        # return the total number of provinces (connected components)
        return province_count

if __name__ == '__main__':
    s = Solution()
    print(s.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))
    print(s.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]))