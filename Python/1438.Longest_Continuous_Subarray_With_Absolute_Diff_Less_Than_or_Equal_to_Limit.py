from collections import deque
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # initialize deque to store minimum values in increasing order
        min_deque = deque()
        # initialize deque to store maximum values in decreasing order
        max_deque = deque()
        
        # length of the input list nums
        n = len(nums)
        # left pointer of the sliding window
        left = 0
        # variable to store the maximum length of valid subarray found so far
        max_length = 0
        
        # iterate over each element in nums using a sliding window technique
        for right in range(n):
            # maintain decreasing order in max_deque
            while max_deque and nums[right] > max_deque[-1]:
                # remove elements from max_deque until the current element is greater 
                # than the last element
                max_deque.pop()
            # add the current element to max_deque
            max_deque.append(nums[right])
            
            # maintain increasing order in min_deque
            while min_deque and nums[right] < min_deque[-1]:
                # remove elements from min_deque until the current element is smaller
                # than the last element
                min_deque.pop()
            # Add the current element to min_deque
            min_deque.append(nums[right])
            
            # check if the current window is invalid (i.e., difference between max and min exceeds limit)
            while max_deque and min_deque and max_deque[0] - min_deque[0] > limit:
                # slide the left pointer to make the window valid again
                if nums[left] == max_deque[0]:
                    # remove the leftmost element from max_deque if it's the same as nums[left]
                    max_deque.popleft()
                if nums[left] == min_deque[0]:
                    # remove the leftmost element from min_deque if it's the same as nums[left]
                    min_deque.popleft()
                
                # increment the left pointer to slide the window to the right
                left += 1 
            
            # update the maximum length of valid subarray found so far
            # calculate the current window size and update max_length if necessary
            max_length = max(max_length, right - left + 1)  
        
        # return the maximum length of a subarray where the difference between 
        # max and min values <= limit
        return max_length

if __name__ == '__main__':
    s = Solution()
    print(s.longestSubarray([8,2,4,7], 4))
    print(s.longestSubarray([10,1,2,4,7,2], 5))
    print(s.longestSubarray([4,2,2,2,4,4,2,2], 0))
