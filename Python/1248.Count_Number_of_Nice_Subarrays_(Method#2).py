from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
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
    print(s.numberOfSubarrays([2,2,2,1,2,2,1,2,2,2], 2))
    print(s.numberOfSubarrays([1,1,2,1,1], 3))
    print(s.numberOfSubarrays([2,4,6], 1))