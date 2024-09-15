from typing import List
from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # initialize a graph as a dictionary where each key maps to another dictionary
        graph = defaultdict(dict)
        
        # populate the graph with equations and their corresponding values
        for (u, v), val in zip(equations, values):
            # ensure both nodes u and v are in the graph
            if u not in graph:
                graph[u] = {}
            if v not in graph:
                graph[v] = {}
            
            # add the directed edge u -> v with weight val
            graph[u][v] = val
            # add the reverse edge v -> u with weight 1/val
            graph[v][u] = 1 / val
        
        # define a helper function DFS to find the path from src to dst
        def dfs(src, dst, visited):
            # if either source or destination is not in the graph, return -1.0 (indicating no path)
            if src not in graph or dst not in graph:
                return -1.0
            
            # if the source is the same as the destination, return 1.0 (the value of a variable to itself is 1)
            if src == dst:
                return 1.0
            
            # mark the current node as visited
            visited.add(src)
            
            # traverse all neighbors of the current node
            for neighbor, value in graph[src].items():
                # skip the neighbor if it has already been visited
                if neighbor in visited:
                    continue
                
                # recursively perform DFS to find the result from the neighbor to the destination
                result = dfs(neighbor, dst, visited)
                
                # if a valid result is found, return the accumulated value (current edge value multiplied by the result)
                if result != -1.0:
                    return value * result
            
            # if the destination is not reachable, return -1.0
            return -1.0
        
        # initialize an empty list to store the results of each query
        results = []
        
        # process each query to find the result using DFS
        for query in queries:
            # append the result of DFS for the current query to the results list
            results.append(dfs(query[0], query[1], set()))
        
        # return the list of results for all queries
        return results

if __name__ == '__main__':
    s = Solution()
    print(s.calcEquation([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))
    print(s.calcEquation([["a","b"],["b","c"],["bc","cd"]], [1.5,2.5,5.0], [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]))
    print(s.calcEquation([["a","b"]], [0.5], [["a","b"],["b","a"],["a","c"],["x","y"]]))