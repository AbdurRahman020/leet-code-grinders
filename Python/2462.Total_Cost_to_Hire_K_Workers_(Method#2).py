from typing import List
from collections import deque
from heapq import heapify, heapreplace

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # initialize the total cost to 0
        total_cost = 0
        
        # if there are not enough elements to select 'k' elements while considering 'candidates'
        if candidates*2 + k > len(costs):
            # simply sort all costs and return the sum of the smallest 'k' costs
            return sum(sorted(costs)[:k])
        
        # initialize a deque with the list of costs for efficient pop operations
        cost_queue = deque(costs)
        
        # initialize heaps (min-heaps) for the left and right parts 'candidates' elements 
        # will be taken from each end of the deque
        # pop elements from the end of deque to form the right heap
        heap_left = [cost_queue.popleft() for _ in range(candidates)]
        # pop elements from the front of deque to form the left heap
        heap_right = [cost_queue.pop() for _ in range(candidates)]
        
        # convert lists into heaps
        heapify(heap_left)
        heapify(heap_right)
        
        # process 'k' elements by always choosing the smaller root from either heap
        for _ in range(k):
            # decide whether to pop from the right heap or the left heap based on their roots
            choose_heap_right = heap_right[0] < heap_left[0]
            # add the smallest element from the chosen heap to the total cost
            total_cost += heapreplace(heap_right if choose_heap_right else heap_left, 
                                      cost_queue.pop() if choose_heap_right else cost_queue.popleft())
        
        # return the total cost after selecting 'k' elements
        return total_cost

if __name__ == '__main__':
    s = Solution()
    print(s.totalCost([17,12,10,2,7,2,11,20,8], 3, 4))
    print(s.totalCost([1,2,4,1], 3, 3))