from typing import List
import heapq

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # convert the input list `nums` into a min-heap in-place
        heapq.heapify(nums)
        
        # initialize an empty list to store sorted elements
        sorted_nums = []
        
        # continue until all elements are popped from the heap
        while nums:
            # pop the smallest element from the heap and append it to `sorted_nums`
            sorted_nums.append(heapq.heappop(nums))
        
        # return the sorted list
        return sorted_nums

if __name__ == '__main__':
    s = Solution()
    print(s.sortArray([5,2,3,1]))
    print(s.sortArray([5,1,1,2,0,0]))