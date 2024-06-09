from typing import List
from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # constructing the graph, using defaultdict to handle unseen nodes
        graph = defaultdict(list)
        # for each connection, adding both directions to represent undirected edges
        # in the tuple, the second element indicates whether the edge direction needs 
        # to be reversed
        for u, v in connections:
            graph[u].append((v, True))  # True indicates it needs to be reversed
            graph[v].append((u, False)) # False indicates no reversal needed
        
        # DFS function to traverse the graph and count reversals
        def dfs(node, visited):
            # marking the current node as visited
            visited.add(node)
            # count of edges that need to be reversed
            reversal_count = 0
            for neighbour, to_reverse in graph[node]:
                # if neighbour hasn't been visited yet
                if neighbour not in visited:
                    # increment the reversal count if needed
                    reversal_count += to_reverse
                    # recursively traverse the neighbour
                    reversal_count += dfs(neighbour, visited)
            
            # return the total count of reversals in the DFS traversal
            return reversal_count
        
        # starting DFS from node 0 and returning the total count of reversals
        visited = set()
        return dfs(0, visited)

if __name__ == '__main__':
    s = Solution()
    print(s.minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]))
    print(s.minReorder(5, [[1,0],[1,2],[3,2],[3,4]]))
    print(s.minReorder(3, [[1,0],[2,0]]))