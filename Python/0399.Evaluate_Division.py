from typing import List
from collections import defaultdict, deque

class DSU:
    def __init__(self):
        # initialize a dictionary to keep track of the parent of each node
        self.node_tree = {}
        # initialize a dictionary to keep track of the value ratio for each node
        self.val = defaultdict(lambda: 1)
    
    def find(self, node: str) -> str:
        # if the node is not in the node_tree, add it with itself as its own parent
        if node not in self.node_tree:
            self.node_tree[node] = node
        
        # path compression: recursively find the root parent and update the parent of the node
        if node != self.node_tree[node]:
            self.node_tree[node] = self.find(self.node_tree[node])
        
        # return the root parent of the node
        return self.node_tree[node]
    
    def union(self, node1: str, node2: str, q: float) -> None:
        # find the root parent of both nodes
        par_node1, par_node2 = self.find(node1), self.find(node2)
        # calculate the ratio between node1 and node2
        ratio = self.val[node2] * q / self.val[node1]
        
        # update the parent and ratio for all nodes connected to par_node1
        for node, par in self.node_tree.items():
            if par == par_node1:
                # update the parent of the node to par_node2
                self.node_tree[node] = par_node2
                # update the ratio for the node
                self.val[node] *= ratio

class Solution:
    def calcEquation1(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
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
    
    def calcEquation2(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
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
    
    def calcEquation3(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # initialize a DSU (Disjoint Set Union) instance
        uf = DSU()
        
        # process each equation and its value to unite nodes and update ratios
        for (u, v), val in zip(equations, values):
            uf.union(u, v, val)
        
        # initialize an empty list to store results of queries
        results = []
        
        # process each query
        for p, q in queries:
            # check if either p or q is not in the DSU or if they are not connected
            if p not in uf.val or q not in uf.val or uf.find(p) != uf.find(q):
                # if not connected, append -1.0 to results
                results.append(-1.0)
            else:
                # if connected, append the ratio of values p/q to results
                results.append(uf.val[p] / uf.val[q])
        
        # return the list of results for all queries
        return results

if __name__ == '__main__':
    s = Solution()
    
    print(s.calcEquation1([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))
    print(s.calcEquation1([["a","b"],["b","c"],["bc","cd"]], [1.5,2.5,5.0], [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]))
    print(s.calcEquation1([["a","b"]], [0.5], [["a","b"],["b","a"],["a","c"],["x","y"]]))
    
    print(s.calcEquation2([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))
    print(s.calcEquation2([["a","b"],["b","c"],["bc","cd"]], [1.5,2.5,5.0], [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]))
    print(s.calcEquation2([["a","b"]], [0.5], [["a","b"],["b","a"],["a","c"],["x","y"]]))
    
    print(s.calcEquation3([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))
    print(s.calcEquation3([["a","b"],["b","c"],["bc","cd"]], [1.5,2.5,5.0], [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]))
    print(s.calcEquation3([["a","b"]], [0.5], [["a","b"],["b","a"],["a","c"],["x","y"]]))
