from typing import List
from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # create a defaultdict to store the graph where each node has a dictionary of (neighbor, direction) pairs
        graph = defaultdict(dict)
        
        # populate the graph with connections, indicating the direction of each edge
        for u, v in connections:
            # u -> v is a "real" edge that needs to be reordered
            graph[u][v] = 1
            # v -> u is a reverse edge that does not need to be reordered
            graph[v][u] = 0
        
        # define a depth-first search (DFS) function to traverse the graph
        def dfs(current_city, reorder_count):
            # mark the current node as visited
            visited.add(current_city)
            
            # traverse neighbors of the current node in the graph
            for neighbor_city, direction in graph[current_city].items():
                # if neighbor_city hasn't been visited, process it
                if neighbor_city not in visited:
                    # increment the reorder_count if the edge is a "real" edge that needs reordering
                    if direction == 1:
                        reorder_count[0] += 1
                    # recursively perform DFS on the neighbor_city
                    dfs(neighbor_city, reorder_count)
        
        # initialize set to track visited nodes during DFS
        visited = set()   
        # initialize list to store the count of edges that need to be reordered
        reorder_count = [0]
        
        # perform DFS starting from node 0
        dfs(0, reorder_count)
        
        # return the total count of edges that need to be reordered
        return reorder_count[0]

if __name__ == '__main__':
    s = Solution()
    print(s.minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]))
    print(s.minReorder(5, [[1,0],[1,2],[3,2],[3,4]]))
    print(s.minReorder(3, [[1,0],[2,0]]))