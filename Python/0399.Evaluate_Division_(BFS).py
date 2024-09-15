from typing import List
from collections import defaultdict, deque

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
        
        # define a helper function BFS to find the path from src to dst
        def bfs(src, dst):
            # if either source or destination is not in the graph, return -1.0 (indicating no path)
            if src not in graph or dst not in graph:
                return -1.0
            
            # initialize visited set to keep track of visited nodes
            visited = set()
            # initialize a queue with the source node and the initial value of 1.0 (representing the multiplication identity)
            queue = deque([(src, 1.0)])
            
            # perform BFS to find the path from src to dst
            while queue:
                # dequeue an element from the queue
                node, curr_val = queue.popleft()
                # if the current node is the destination, return the current accumulated value
                if node == dst:
                    return curr_val
                
                # mark the current node as visited
                visited.add(node)
                # traverse all neighbors of the current node
                for neighbor, edge_val in graph[node].items():
                    # if the neighbor has not been visited, enqueue it with the updated accumulated value
                    if neighbor not in visited:
                        queue.append((neighbor, curr_val * edge_val))
            
            # if destination is not reachable, return -1.0
            return -1
        
        # initialize an empty list to store the results of each query
        results = []
        
        # process each query to find the result using BFS
        for p, q in queries:
            results.append(bfs(p, q))
        
        # return the list of results for all queries
        return results

if __name__ == '__main__':
    s = Solution()
    print(s.calcEquation([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))
    print(s.calcEquation([["a","b"],["b","c"],["bc","cd"]], [1.5,2.5,5.0], [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]))
    print(s.calcEquation([["a","b"]], [0.5], [["a","b"],["b","a"],["a","c"],["x","y"]]))