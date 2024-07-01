from typing import List
from collections import defaultdict, deque

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # build a graph using defaultdict of dictionaries
        graph = defaultdict(dict)
        
        # populate the graph with connections and their directions
        for u, v in connections:
            # u -> v is a "real" edge that needs to be reordered
            graph[u][v] = 1
            # v -> u is a reverse edge that does not need to be reordered
            graph[v][u] = 0
        
        # initialize total count of edges that need to be reordered
        reorder_count = 0  
        # initialize set to track visited cities
        visited = set()
        # initialize queue for BFS starting from city 0
        queue = deque([0])
        
        # perform BFS to traverse the graph
        while queue:
            current_city = queue.popleft()
            
            # skip cities that have already been visited
            if current_city in visited:
                continue
            
            # mark current city as visited
            visited.add(current_city)
            
            # traverse neighbors of the current city in the graph
            for neighbor_city, direction in graph[current_city].items():
                # if neighbor city hasn't been visited, process it
                if neighbor_city not in visited:
                    # accumulate the count of edges that need to be reordered
                    reorder_count += direction
                    # add neighbor city to the queue for further exploration
                    queue.append(neighbor_city)
        
        # return the total count of edges that need to be reordered
        return reorder_count

if __name__ == '__main__':
    s = Solution()
    print(s.minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]))
    print(s.minReorder(5, [[1,0],[1,2],[3,2],[3,4]]))
    print(s.minReorder(3, [[1,0],[2,0]]))