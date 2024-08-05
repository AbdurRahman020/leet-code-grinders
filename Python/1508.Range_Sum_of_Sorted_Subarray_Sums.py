from typing import List

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        # define a constant for the modulo operation to prevent integer overflow
        MODULO = 10**9 + 7
        # initialize a list to hold the sums of all possible subarrays
        sub_arr_sum = []
        
        # loop over each starting index of the subarray
        for i in range(n):
            # initialize the current sum of the subarray starting at index i
            curr_sum  = 0
            
            # loop over each ending index of the subarray starting from index i
            for j in range(i, n):
                # add the value of the current element to the current sum
                curr_sum  += nums[j]
                # append the current sum to the list of subarray sums
                sub_arr_sum.append(curr_sum)
        
        # sort the list of subarray sums in ascending order
        sub_arr_sum.sort()
        
        # compute the sum of subarray sums from index (left-1) to (right-1) inclusive
        # the range left-1 to right is inclusive, so slicing is sub_arr_sum[left - 1:right]
        # apply modulo operation to ensure the result does not exceed the limit
        return sum(sub_arr_sum[left - 1: right]) % MODULO

if __name__ == '__main__':
    s = Solution()
    print(s.rangeSum([1,2,3,4], 4, 1, 5))
    print(s.rangeSum([1,2,3,4], 4, 3, 4))
    print(s.rangeSum([1,2,3,4], 4, 1, 10))