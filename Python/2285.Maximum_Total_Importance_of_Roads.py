from typing import List
import heapq

class Solution:
    def maximumImportance1(self, n: int, roads: List[List[int]]) -> int:
        # initialize frequency array to count connections for each node
        freq = [0] * n
        
        # calculate the frequency of connections for each node
        for road in roads:
            freq[road[0]] += 1
            freq[road[1]] += 1
        
        # using negative values to simulate max heap
        max_heap = [-f for f in freq]
        # convert the list into a heap in-place
        heapq.heapify(max_heap)
        
        # calculate the maximum importance
        maximum_importance = 0
        # starting value for current weight (n, n-1, ..., 1)
        curr_val = n
        
        while max_heap:
            # extract the maximum frequency from the heap
            f = -heapq.heappop(max_heap)
            # add to the total importance
            maximum_importance += curr_val * f
            # decrease the weight for the next node
            curr_val -= 1
        
        return maximum_importance
    
    def maximumImportance2(self, n: int, roads: List[List[int]]) -> int:
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
    
    print(s.maximumImportance1(5, [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]))
    print(s.maximumImportance1(5, [[0,3],[2,4],[1,3]]))
    
    print(s.maximumImportance2(5, [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]))
    print(s.maximumImportance2(5, [[0,3],[2,4],[1,3]]))
