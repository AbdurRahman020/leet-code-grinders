from typing import List
from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        leaves = deque(node for node in graph if len(graph[node]) == 1)

        while n > 2:
            n -= len(leaves)
            for _ in range(len(leaves)):
                leaf = leaves.popleft()
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    leaves.append(neighbor)
        
        return list(leaves)

if __name__ == '__main__':
    s = Solution()
    print(s.findMinHeightTrees(4, [[1,0],[1,2],[1,3]]))
    print(s.findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]]))