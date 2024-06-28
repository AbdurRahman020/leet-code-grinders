from typing import List

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        # initialize a list to store the degree (number of connections) of each node
        in_degrees = [0] * n
        
        # calculate the in-degree for each node based on the given roads
        for u, v in roads:
            # increment the in-degree of node u
            in_degrees[u] += 1
            # increment the in-degree of node v
            in_degrees[v] += 1
        
        # sort the in-degrees list
        in_degrees.sort()
        
        # calculate and return the maximum importance
        return sum((i + 1) * v for i, v in enumerate(in_degrees))

if __name__ == '__main__':
    s = Solution()
    print(s.maximumImportance(5, [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]))
    print(s.maximumImportance(5, [[0,3],[2,4],[1,3]]))