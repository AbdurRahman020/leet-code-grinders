from typing import List

class DSU:
    def __init__(self, n: int) -> None:
        # parent array to track representatives
        self.parent = list(range(n + 1))
        # rank to optimize union by rank
        self.rank = [0] * (n + 1)
        # count of components
        self.component_count = n
    
    def find(self, u: int) -> int:
        if self.parent[u] != u:
            # recursive find and flatten path
            self.parent[u] = self.find(self.parent[u])
        
        # return the root of the set containing u
        return self.parent[u]
    
    def union(self, u: int, v: int) -> bool:
        # find the roots of u and v
        root_u, root_v = self.find(u), self.find(v)
        
        if root_u == root_v:
            # u and v are already in the same set
            return False
        
        # union by rank: attach smaller tree under larger tree to keep the tree flat
        if self.rank[root_u] < self.rank[root_v]:
            # ensure root_u is the root of the larger tree
            root_u, root_v = root_v, root_u
        
        # attach root_v under root_u
        self.parent[root_v] = root_u
        
        if self.rank[root_u] == self.rank[root_v]:
            # increment rank of root_u
            self.rank[root_u] += 1
        
        # decrease the number of components
        self.component_count -= 1
        
        # successfully merged u and v into one set
        return True

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # initialize DSU instances for Alice and Bob
        alice, bob = DSU(n), DSU(n)
        remaining_edges = len(edges)
        
        # iterate over edges
        for t, u, v in filter(lambda x: x[0] == 3, edges):
            if t == 3:
                # type 3 edges: try to union both DSUs (Alice and Bob)
                remaining_edges -= alice.union(u, v) | bob.union(u, v)
        
        # iterate over edges again
        for t, u, v in filter(lambda x: x[0] in (1, 2), edges):
            if t == 2:
                # type 2 edges: apply union operation on Bob's DSU
                remaining_edges -= bob.union(u, v)
            else:
                # type 1 edges: apply union operation on Alice's DSU
                remaining_edges -= alice.union(u, v)
        
        # check if both Alice and Bob have exactly one component each
        return remaining_edges if (alice.component_count == 1 and bob.component_count == 1) else -1

if __name__ == '__main__':
    s = Solution()
    print(s.maxNumEdgesToRemove(4, [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]))
    print(s.maxNumEdgesToRemove(4, [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]))
    print(s.maxNumEdgesToRemove(4, [[3,2,3],[1,1,2],[2,3,4]]))