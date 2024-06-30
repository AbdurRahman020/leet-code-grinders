from typing import List
from collections import defaultdict

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
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
    print(s.getAncestors(8, [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]))
    print(s.getAncestors(5, [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]))