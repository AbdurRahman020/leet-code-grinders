from typing import List
from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited_node = set()

        def dfs(node):
            if node == destination:
                return True
            
            visited_node.add(node)
            for path_next in graph[node]:
                if path_next not in visited_node and dfs(path_next):
                    return True
                
            return False
        
        return dfs(source)

if __name__ == '__main__':
    s = Solution()
    print(s.validPath(3, [[0,1],[1,2],[2,0]], 0, 2))
    print(s.validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5))