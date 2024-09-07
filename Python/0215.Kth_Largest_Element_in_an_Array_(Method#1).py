from typing import List
from heapq import heapify, heappop, heappush

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # initialize a min-heap with the first k elements from nums
        heap = nums[:k]
        # transform the list into a heap in-place
        heapify(heap)
        
        # iterate over the remaining elements in the list
        for num in nums[k:]:
            # if the current number is larger than the smallest element in the heap
            if num > heap[0]:
                # remove the smallest element from the heap
                heappop(heap)
                # add the current number to the heap
                heappush(heap, num)
        
        # the root of the heap (the smallest element in the min-heap) is the k-th largest element
        return heap[0]
    
    # one line code
    # return heapq.nlargest(k, nums)[-1] 

if __name__ == '__main__':
    s = Solution()
    print(s.findKthLargest([3,2,1,5,6,4], 2))
    print(s.findKthLargest([3,2,3,1,2,4,5,5,6], 4))