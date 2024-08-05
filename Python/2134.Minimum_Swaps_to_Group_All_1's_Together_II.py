from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        # get the length of the input array
        array_length = len(nums)
        
        # calculate the total number of 1s in the array
        total_ones = sum(nums)
        
        # compute the number of zeros in the initial window of size `total_ones`, this is
        # achieved by subtracting the sum of the first `total_ones` elements from `total_ones`
        initial_zeros = total_ones - sum(nums[:total_ones])
        
        # initialize `min_zeros` and `current_zeros` with the number of zeros in the initial window
        min_zeros = curr_zeros = initial_zeros
        
        # iterate over the array to slide the window and find the minimum number of zeros
        for i in range(array_length):
            # determine the new element entering the window (circular array access)
            new_element = nums[(i + total_ones) % array_length]
            if new_element == 0:
                # if the new element is 0, increment `current_zeros`
                curr_zeros += 1
            
            # determine the element that is leaving the window
            outgoing_element = nums[i]
            if outgoing_element == 0:
                # if the outgoing element is 0, decrement `current_zeros`
                curr_zeros -= 1
            
            # update `min_zeros` to the minimum of its current value and `current_zeros`
            min_zeros = min(min_zeros, curr_zeros)
        
        # return the minimum number of zeros found in any window of size `total_ones`
        return min_zeros

if __name__ == '__main__':
    s = Solution()
    print(s.minSwaps([0,1,0,1,1,0,0]))
    print(s.minSwaps([0,1,1,1,0,0,1,1,0]))
    print(s.minSwaps([1,1,0,0,1]))