from typing import List
import heapq

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
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

if __name__ == '__main__':
    s = Solution()
    # Example usage
    print(s.maximumImportance(5, [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]))  # Output: 28
    print(s.maximumImportance(5, [[0,3],[2,4],[1,3]]))  # Output: 14
