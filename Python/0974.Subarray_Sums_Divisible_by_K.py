from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # get the length of the input list
        n = len(nums)
        
        # create a dictionary to store the count of each prefix sum remainder, 
        # initialize with 0 remainder since an empty subarray has a sum divisible by k
        prefix_map = {0: 1}
        # initialize prefix sum to 0
        prefix_sum = 0
        # initialize count of subarrays with sum divisible by k
        subarray_count = 0
        
        # iterate through the input list
        for i in range(n):
            # calculate the prefix sum
            prefix_sum += nums[i]
            # calculate the remainder when the prefix sum is divided by k
            remainder = prefix_sum % k
            
            # if the current remainder has been seen before, increment the count
            # of subarrays with sum divisible by k
            if remainder in prefix_map:
                subarray_count += prefix_map[remainder]
                # update the count of subarrays with the current remainder
                prefix_map[remainder] += 1
            else:
                # if the remainder is not in the prefix_map, add it with count 1
                prefix_map[remainder] = 1
                
        # return the total count of subarrays with sum divisible by k
        return subarray_count

if __name__ == '__main__':
    s = Solution()
    print(s.subarraysDivByK([4,5,0,-2,-3,1], 5))
    print(s.subarraysDivByK([5], 9))