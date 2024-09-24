from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # get the number of houses (elements in nums)
        n = len(nums)
        
        # if there is only one house, return the amount in that house
        if n == 1:
            return nums[0]
        
        # initialize a list to store the maximum amounts that can be robbed
        dp = [0] * n
        
        # base case: the maximum amount that can be robbed from the first house
        dp[0] = nums[0]
        
        # base case: the maximum amount that can be robbed from the first two houses
        dp[1] = max(nums[0], nums[1])
        
        # iterate through the houses starting from the third house
        for i in range(2, n):
            # for each house, decide whether to rob it or not
            # if we rob this house, we cannot rob the previous one (dp[i-2])
            # if we do not rob this house, we take the maximum from the previous house (dp[i-1])
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        # the last element in dp contains the maximum amount that can be robbed
        return dp[n-1]

if __name__ == '__main__':
    s = Solution()
    print(s.rob([1,2,3,1]))
    print(s.rob([2,7,9,3,1]))