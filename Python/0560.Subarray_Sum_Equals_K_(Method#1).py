from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # initialize the result variable to store the count of subarrays
        result = 0
        # initialize the prefix sum variable
        prefix_sum = 0
        # initialize a dictionary to store the count of prefix sums encountered, also
        # initialize it with 0:1 to handle cases where the prefix sum equals k
        sum_count = {0: 1}
        
        # iterate through the elements of the input list nums
        for num in nums:
            # update the prefix sum by adding the current number
            prefix_sum += num
            # check if there exists a previous prefix sum such that prefix_sum - k equals that sum
            if prefix_sum - k in sum_count:
                # if such a sum exists, increment the result by the count of occurrences of that sum 
                result += sum_count[prefix_sum-k]
            
            # if the prefix sum is encountered for the first time, initialize its count to 1
            if prefix_sum not in sum_count:
                sum_count[prefix_sum] = 1
            # otherwise, increment its count
            else:
                sum_count[prefix_sum] += 1
        
        # return the final count of subarrays
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.subarraySum([1,1,1], 2))
    print(s.subarraySum([1,2,3], 3))