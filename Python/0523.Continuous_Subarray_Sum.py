from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # dictionary to store remainder and its corresponding index, initialize with 0 
        # to handle the case where sum % k == 0
        remainder_index = {0: -1}
        # variable to store cumulative sum of nums
        total_sum = 0  

        # iterate through nums list along with index
        for i, num in enumerate(nums):
            # add the current number to total_sum
            total_sum += num
            # calculate the remainder when divided by k
            remainder = total_sum % k

            # if the current remainder is not in the remainder_index dictionary
            if remainder not in remainder_index:
                # store the remainder and its corresponding index
                remainder_index[remainder] = i
            # if the current remainder is already in the dictionary
            elif i - remainder_index[remainder] > 1:
                # if the difference between the current index and the index of the previous
                # occurrence of the same remainder is greater than 1, it means there is
                # a subarray whose sum is divisible by k and has at least two elements
                return True

        # if no such subarray is found, return False
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.checkSubarraySum([23,2,6,4,7], 13))
    print(s.checkSubarraySum([23,2,6,4,7], 6))
    print(s.checkSubarraySum([23,2,4,6,7], 6))