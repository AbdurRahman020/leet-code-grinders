from typing import List
from heapq import heappop, heappush

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # initialize the sum of the current k elements and the maximum score found
        curr_sum = max_sum = 0
        
        # create an empty min-heap to maintain the k largest elements from nums1
        heap = []
        
        # iterate through the sorted pairs of (nums2[i], nums1[i]), sorting is done in
        # descending order based on nums2
        for nums2, nums1 in sorted(zip(nums2, nums1), reverse=True):
            # push the current element from nums1 into the min-heap
            heappush(heap, nums1)
            
            # add the current nums1 element to the current sum
            curr_sum += nums1
            
            # if the heap exceeds size k, remove the smallest element from the heap
            # and subtract it from the current sum
            if len(heap) > k:
                curr_sum -= heappop(heap)
            
            # if the heap size is exactly k, calculate the score and update the max_sum
            # the score is curr_sum * nums2, where nums2 is the current factor from the sorted list
            if len(heap) == k:
                max_sum = max(max_sum, curr_sum * nums2)
        
        # return the maximum score found
        return max_sum

if __name__ == '__main__':
    s = Solution()
    print(s.maxScore([1,3,3,2], [2,1,3,4], 3))
    print(s.maxScore([4,2,3,1,1], [7,5,10,9,6], 1))