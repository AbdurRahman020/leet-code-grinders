from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # initialize left_sum to 0 and right_sum to the sum of all elements in nums
        left_sum, right_sum = 0, sum(nums)
        
        # iterate through each element in nums along with its index
        for i, num in enumerate(nums):
            # decrease right_sum by the current element value
            right_sum -=num
            
            # if left_sum equals right_sum, return the current index
            if left_sum == right_sum:
                return i
            
            # increase left_sum by the current element value for the next iteration
            left_sum += num
        
        # if no pivot index is found, return -1
        return -1

if __name__ == '__main__':
    s = Solution()
    print(s.pivotIndex([1,7,3,6,5,6]))
    print(s.pivotIndex([1,2,3]))
    print(s.pivotIndex([2,1,-1]))