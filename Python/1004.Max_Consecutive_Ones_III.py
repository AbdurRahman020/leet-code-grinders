from typing import List

class Solution:
    def longestOnes(self, nums: List[int], allowedFlips: int) -> int:
        # initialize the start and end pointers of the sliding window
        window_start = window_end = 0
        
        # iterate over each element with the window_end pointer
        for window_end in range(len(nums)):
            # if the current element is 0, decrement the number of allowed flips
            if nums[window_end] == 0:
                allowedFlips -= 1
            
            # if we have used more flips than allowed
            if allowedFlips < 0:
                # if the element at window_start is 0, increment allowedFlips (since we 
                # are removing it from the window)
                if nums[window_start] == 0:
                    allowedFlips += 1
                
                # move the start pointer to the right, shrinking the window from the left
                window_start += 1
        
        # return the length of the longest window where the number of flips needed is 
        # within the allowed limit
        return window_end - window_start + 1

if __name__ == '__main__':
    s = Solution()
    print(s.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
    print(s.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))