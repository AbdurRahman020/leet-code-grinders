from typing import List
from collections import defaultdict

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
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
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
    print(s.calcEquation([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))
    print(s.calcEquation([["a","b"],["b","c"],["bc","cd"]], [1.5,2.5,5.0], [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]))
    print(s.calcEquation([["a","b"]], [0.5], [["a","b"],["b","a"],["a","c"],["x","y"]]))