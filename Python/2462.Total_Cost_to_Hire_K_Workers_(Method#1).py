from typing import List
from heapq import heappush, heappop

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # initialize pointers for the left and right ends of the costs list
        left_ptr, right_ptr = 0, len(costs) - 1
        # initialize two heaps to manage the smallest elements from the left and right sides
        left_heap, right_heap = [], []
        # initialize total cost to accumulate the cost of the cheapest k items
        total_cost = 0
        
        # loop to select k cheapest items
        while k > 0:
            # add up to 'candidates' elements from the left side of the list to the left_heap
            while len(left_heap) < candidates and left_ptr <= right_ptr:
                # push current left element to the heap
                heappush(left_heap, costs[left_ptr])
                # move the left pointer to the right
                left_ptr += 1
            
            # add up to 'candidates' elements from the right side of the list to the right_heap
            while len(right_heap) < candidates and left_ptr <= right_ptr:
                # push current right element to the heap
                heappush(right_heap, costs[right_ptr])
                # move the right pointer to the left
                right_ptr -= 1
            
            # determine the minimum cost from the left_heap (if not empty) or set to infinity if empty
            min_left = left_heap[0] if left_heap else float('inf')
            # determine the minimum cost from the right_heap (if not empty) or set to infinity if empty
            min_right = right_heap[0] if right_heap else float('inf')
            
            # add the cheaper of the two minimum costs to the total cost
            total_cost += min_left if min_left <= min_right else min_right
            # remove the selected minimum cost from the corresponding heap
            heappop(left_heap) if min_left <= min_right else heappop(right_heap)
            
            # decrement k, as we have selected one more item
            k -= 1
        
        # return the total cost of the k cheapest items
        return total_cost

if __name__ == '__main__':
    s = Solution()
    print(s.totalCost([17,12,10,2,7,2,11,20,8], 3, 4))
    print(s.totalCost([1,2,4,1], 3, 3))