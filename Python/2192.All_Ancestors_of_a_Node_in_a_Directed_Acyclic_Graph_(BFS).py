from typing import List
from collections import defaultdict, deque

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # create a graph using adjacency list representation
        graph = defaultdict(list)
        # maintain an in-degree array to count incoming edges for each node
        in_degree = [0] * n
        
        # populate the graph and in-degree array based on the edges
        for u, v in edges:
            # u -> v (directed edge)
            graph[u].append(v)
            # increase in-degree of v
            in_degree[v] += 1
        
        # initialize a queue for nodes with zero in-degree
        queue = deque()
        # use a defaultdict to store ancestors for each node
        ancestors = defaultdict(set)

        # Initialize the queue with nodes having zero in-degree
        for i in range(n):
            if in_degree[i] == 0:
                # add nodes with zero in-degree to the queue, along with an empty set for ancestors
                queue.append([i, set()])
        
        # perform topological sorting using Kahn's algorithm
        while queue:
            # dequeue a node with zero in-degree
            node, ancestors_of_node = queue.popleft()
            # traverse through all adjacent nodes of the dequeued node
            for adj_node in graph[node]:
                # decrease the in-degree of adjacent nodes
                in_degree[adj_node] -= 1
                # update ancestors of adjacent nodes:
                # adj_node inherits ancestors of node and node itself as its ancestor
                ancestors[adj_node].add(node)
                ancestors[adj_node].update(ancestors_of_node)
                # if the in-degree of an adjacent node becomes zero, enqueue it
                if in_degree[adj_node] == 0:
                    queue.append([adj_node, ancestors[adj_node]])
        
        # construct the result based on ancestors dictionary
        result = []
        for i in range(n):
            if i in ancestors:
                # convert set to sorted list for each node's ancestors
                result.append(sorted(list(ancestors[i])))
            else:
                # if a node has no ancestors, append an empty list
                result.append([])
        
        # return the list of ancestors for each vertex
        return result 

if __name__ == '__main__':
    s = Solution()
    print(s.getAncestors(8, [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]))
    print(s.getAncestors(5, [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]))