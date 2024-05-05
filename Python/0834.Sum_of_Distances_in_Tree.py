from collections import defaultdict

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: list[list[int]]) -> list[int]:
        # graph construction
        graph = defaultdict(list)
        for u, v in edges:
            # adding edges bidirectionally
            graph[u].append(v)
            graph[v].append(u)
        
        # list to store subtree sizes
        sub_tree_sizes = [0 for _ in range(n)]
        # list to store depths of nodes
        depths = [0 for _ in range(n)]
        # first Depth-First Search to calculate subtree sizes and depths
        def dfs1(parent, curr, curr_depth):
            # initializing subtree size of current node
            curr_sub_tree_size = 1
            # traversing neighbors of current node
            for neighbor in graph[curr]:
                # if the neighbor is the parent, skip
                if neighbor == parent:
                    continue
                # recursively calculate subtree sizes and update current subtree size
                curr_sub_tree_size += dfs1(curr, neighbor, curr_depth + 1)
            
            # storing current subtree size and depth
            sub_tree_sizes[curr] = curr_sub_tree_size
            depths[curr] = curr_depth

            return curr_sub_tree_size
        
        # initializing array to store the final answer
        ans = [0 for _ in range(n)]
        # second Depth-First Search to calculate sum of distances for each node
        def dfs2(parent, curr, curr_sum_distance):
            # storing sum of distances for current node
            ans[curr] = curr_sum_distance
            # traversing neighbors of current node
            for neighbor in graph[curr]:
                # if the neighbor is the parent, skip
                if neighbor == parent:
                    continue
                # recursively calculate sum of distances for neighbors
                dfs2(curr, neighbor, curr_sum_distance + n - 2 * sub_tree_sizes[neighbor])
        
        # perform the first DFS from the root node
        dfs1(-1, 0, 0)
        # perform the second DFS to compute the sum of distances for each node
        dfs2(-1, 0, sum(depths))

        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.sumOfDistancesInTree(6, [[0,1],[0,2],[2,3],[2,4],[2,5]]))
    print(s.sumOfDistancesInTree(1, []))
    print(s.sumOfDistancesInTree(2, [[1,0]]))