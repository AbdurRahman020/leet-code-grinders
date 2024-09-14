from typing import List
from collections import defaultdict

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # get the total number of cities (nodes in the graph)
        total_cities = len(isConnected)
        
        # create a graph representation using adjacency list
        graph = defaultdict(list)
        
        # build the graph based on the isConnected matrix
        for u in range(total_cities):
            for v in range(u + 1, total_cities):
                # if there is a connection between city u and city v
                if isConnected[u][v] == 1:
                    # add v to the adjacency list of u
                    graph[u].append(v)
                    # add u to the adjacency list of v (undirected graph)
                    graph[v].append(u)
        
        # initialize a list to track visited cities
        city_visited = [False] * total_cities
        
        # define a DFS function to explore connected components
        def dfs(city):
            # explore all neighbors of the current city
            for neighbor in graph[city]:
                # if the neighbor city has not been visited
                if city_visited[neighbor] == False:
                    # mark the neighbor city as visited
                    city_visited[neighbor] = True
                    # recursively perform DFS on the neighbor city
                    dfs(neighbor)
        
        # initialize the count of provinces (connected components)
        province_count = 0
        
        # iterate through each city
        for city in range(total_cities):
            # if the city has not been visited yet
            if city_visited[city] == False:
                # increment the province count
                province_count += 1
                # mark the current city as visited
                city_visited[city] = True
                # perform DFS starting from the current city
                dfs(city)
        
        # return the total number of provinces (connected components)
        return province_count

if __name__ == '__main__':
    s = Solution()
    print(s.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))
    print(s.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]))