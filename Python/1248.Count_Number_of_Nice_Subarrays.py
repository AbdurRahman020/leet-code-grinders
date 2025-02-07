from typing import List
from collections import deque

class Solution:
    def numberOfSubarrays1(self, nums: List[int], k: int) -> int:
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
    
    def numberOfSubarrays2(self, nums: List[int], k: int) -> int:
        # convert nums to an array of 0s and 1s where 1 represents odd numbers
        nums_mod = [num % 2 for num in nums]
        # initialize prefix_counts array
        prefix_counts = [0] * (len(nums_mod) + 1)
        # start with 1 because at the beginning we have 0 odd numbers
        prefix_counts[0] = 1
        # initialize the number of odd numbers encountered
        odd_count = 0
        # initialize the number of subarrays with exactly k odd numbers
        subarray_count = 0
        
        # iterate through nums_mod array
        for num in nums_mod:
            if num == 1:
                # increment odd_count for each odd number encountered
                odd_count += 1
            
            # check if there are at least k odd numbers seen so far
            if odd_count >= k:
                subarray_count += prefix_counts[odd_count - k]
            
            # increment the count of current odd_count in prefix_counts
            prefix_counts[odd_count] += 1
        
        # return the total count of subarrays with exactly k odd numbers
        return subarray_count

if __name__ == '__main__':
    s = Solution()
    
    print(s.numberOfSubarrays1([2,2,2,1,2,2,1,2,2,2], 2))
    print(s.numberOfSubarrays1([1,1,2,1,1], 3))
    print(s.numberOfSubarrays1([2,4,6], 1))
    
    print(s.numberOfSubarrays2([2,2,2,1,2,2,1,2,2,2], 2))
    print(s.numberOfSubarrays2([1,1,2,1,1], 3))
    print(s.numberOfSubarrays2([2,4,6], 1))
