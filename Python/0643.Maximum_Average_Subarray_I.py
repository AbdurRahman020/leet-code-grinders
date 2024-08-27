from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # initialize the sum of the first window of size k
        curr_sum = sum(nums[0:k])
        
        # set the initial maximum sum to be the sum of the first window
        max_sum = curr_sum
        
        # iterate over the array starting from the end of the first window
        for i in range(k, len(nums)):
            # update the current sum by subtracting the element that is sliding out 
            # of the window and adding the element that is sliding into the window
            curr_sum += nums[i] - nums[i-k]
            
            # update max_sum if the new current sum is greater
            if curr_sum > max_sum:
                max_sum = curr_sum
        
        # compute and return the average of the maximum sum found
        return max_sum / k

if __name__ == '__main__':
    s =  Solution()
    print(s.findMaxAverage([1,12,-5,-6,50,3], 4))
    print(s.findMaxAverage([5], 1))