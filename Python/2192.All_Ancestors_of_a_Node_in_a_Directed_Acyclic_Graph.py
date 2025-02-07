from typing import List
from collections import defaultdict, deque

class Solution:
    def getAncestors1(self, n: int, edges: List[List[int]]) -> List[List[int]]:
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
    
    def getAncestors2(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # initialize ancestors as a list of sets, where each set will store ancestors for
        # a vertex
        ancestors = [set() for _ in range(n)]
        
        # create a defaultdict to represent the graph where key is the vertex and value 
        # is a list of its ancestors
        graph = defaultdict(list)
        for u, v in edges:
            graph[v].append(u)
        
        # initialize visited list to track visited vertices during DFS
        visited = [False] * n
        
        # define DFS function to traverse the graph and collect ancestors
        def dfs(curr_vertex):
            # set to store ancestors of current vertex
            curr_ancestors = set()
            # mark current vertex as visited
            visited[curr_vertex] = True
            
            # traverse through all ancestors of current vertex
            for v in graph[curr_vertex]:
                # add ancestor to current ancestors set
                curr_ancestors.add(v)
                # if ancestor vertex is already visited
                if visited[v]:
                    # update current ancestors with ancestors of v
                    curr_ancestors.update(ancestors[v])
                else:
                    # recursively visit ancestors of v
                    curr_ancestors.update(dfs(v))
            
            # update ancestors of current vertex
            ancestors[curr_vertex].update(curr_ancestors)
            
            # return current ancestors set
            return curr_ancestors
        
        # perform DFS for each vertex if it hasn't been visited
        for i in range(n):
            if not visited[i]:
                dfs(i)
        
        # sort each set of ancestors for each vertex
        for i in range(n):
            ancestors[i] = sorted(ancestors[i])
        
        # return the list of ancestors for each vertex
        return ancestors

if __name__ == '__main__':
    s = Solution()
    
    print(s.getAncestors1(8, [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]))
    print(s.getAncestors1(5, [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]))
    
    print(s.getAncestors2(8, [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]))
    print(s.getAncestors2(5, [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]))
