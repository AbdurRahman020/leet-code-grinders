from typing import List
from heapq import heapify, heappop, heappush
from random import choice

class Solution:
    def findKthLargest1(self, nums: List[int], k: int) -> int:
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
    
    def findKthLargest2(self, nums, k):
        # define the quick_select function to perform the selection
        def quick_select(nums, k):
            # randomly select a pivot element from nums
            pivot = choice(nums)
            # initialize lists to hold elements based on comparison with pivot
            left, mid, right = [], [], []
            
            # partition the nums list into left, mid, and right based on pivot
            for num in nums:
                if num > pivot:
                    # elements greater than pivot go to the left
                    left.append(num)
                elif num < pivot:
                    # elements less than pivot go to the right
                    right.append(num)
                else:
                    # elements equal to pivot go to the middle
                    mid.append(num)
            
            # if k is less than or equal to the number of elements in left, recursively search in left
            if k <= len(left):
                return quick_select(left, k)
            
            # if k is greater than the number of elements in left plus mid, search in right with updated k
            if len(left) + len(mid) < k:
                return quick_select(right, k - len(left) - len(mid))
            
            # if k is within the range of mid, the pivot is the k-th largest element
            return pivot
        
        # call the quick_select function with the initial list and k
        return quick_select(nums, k)
    
    # one line code
    # return heapq.nlargest(k, nums)[-1] 

if __name__ == '__main__':
    s = Solution()
    
    print(s.findKthLargest1([3,2,1,5,6,4], 2))
    print(s.findKthLargest1([3,2,3,1,2,4,5,5,6], 4))
    
    print(s.findKthLargest2([3,2,1,5,6,4], 2))
    print(s.findKthLargest2([3,2,3,1,2,4,5,5,6], 4))