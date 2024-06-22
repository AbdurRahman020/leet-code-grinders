from typing import List
from collections import deque

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # deque to store indices of odd numbers
        odd_indices_queue = deque()
        # length of the input list
        n = len(nums)
        
        # collect indices of odd numbers
        for i in range(n):
            if nums[i] % 2 != 0:
                odd_indices_queue.append(i)
        # append n to handle subarrays ending at the last element
        odd_indices_queue.append(n)  
        
        # pointer to track the start of the current window
        window_start = 0
        # counter for the number of subarrays with exactly k odd numbers
        subarray_count = 0
        
        # process the deque to find subarrays with exactly k odd numbers
        while len(odd_indices_queue) > k:
            # start index of the current window
            current_window_start = odd_indices_queue[k-1]
            # start index of the next window
            next_window_start = odd_indices_queue[k]
            
            # calculate subarrays count
            subarray_count += next_window_start - current_window_start
            
            if  window_start == odd_indices_queue[0]:
                # if start pointer matches the first element in deque, pop it
                odd_indices_queue.popleft()
            
            # move the start pointer to the right
            window_start += 1  
        
        # return the total number of subarrays found
        return subarray_count

if __name__ == '__main__':
    s = Solution()
    print(s.numberOfSubarrays([2,2,2,1,2,2,1,2,2,2], 2))
    print(s.numberOfSubarrays([1,1,2,1,1], 3))
    print(s.numberOfSubarrays([2,4,6], 1))