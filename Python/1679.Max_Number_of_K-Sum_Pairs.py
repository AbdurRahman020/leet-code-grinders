from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # sort the list of numbers in non-decreasing order
        nums.sort()
        # initialize a counter to keep track of the number of valid operations
        operations_count = 0
        # initialize two pointers: i starting from the beginning and j from the end of the list
        i, j = 0, len(nums) - 1
        
        # loop until the two pointers meet
        while i < j:
            # calculate the sum of the elements at the two pointers
            curr_sum = nums[i] + nums[j]
            # if the current sum equals the target value k
            if curr_sum == k:
                # increment the count of operations
                operations_count += 1
                # move the left pointer to the right
                i += 1
                # move the right pointer to the left
                j -= 1
            # if the current sum is less than the target value k
            elif curr_sum < k:
                # move the left pointer to the right to increase the sum
                i += 1
            # if the current sum is greater than the target value k
            else:
                # move the right pointer to the left to decrease the sum
                j -= 1
        
        # return the total number of operations found
        return operations_count

if __name__ == '__main__':
    s = Solution()
    print(s.maxOperations([1,2,3,4], 5))
    print(s.maxOperations([3,1,3,4,3], 6))