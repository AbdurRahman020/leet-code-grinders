from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # initialize the start index of the sliding window
        window_start = 0
        # initialize the count of zeros within the window
        zero_count = 0

        # iterate over the array with the end index of the sliding window
        for window_end in range(len(nums)):
            # if the current element is zero, increment the zero count
            if nums[window_end] == 0:
                zero_count += 1
            
            # if the count of zeros exceeds 1, we need to adjust the start of the window
            if zero_count > 1:
                # move the start index of the window to the right
                # if the element at the start of the window was zero, decrement the zero count
                if nums[window_start] == 0:
                    zero_count -= 1
                
                # shift the start of the window right by one position
                window_start += 1
        
        # the length of the longest valid subarray with at most one zero is given by 
        # the difference between the end index of the window (window_end) and the start 
        # index of the window (window_start)
        # the `window_end` index is the current position in the array, while `window_start` 
        # marks the beginning of the valid subarray
        # therefore, the length of the valid subarray is calculated as: `window_end - window_start`
        return window_end - window_start

if __name__ == '__main__':
    s = Solution()
    print(s.longestSubarray([1,1,0,1]))
    print(s.longestSubarray([0,1,1,1,0,1,1,0,1]))
    print(s.longestSubarray([1,1,1]))