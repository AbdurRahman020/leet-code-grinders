from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # get the length of the cost list
        n = len(cost)
        # initialize a list dp to store the minimum cost up to each step
        dp = [0] * (n + 1)
        # base cases: the cost to reach the first and second step
        dp[0], dp[1] = cost[0], cost[1]
        
        # iterate through the cost list starting from the 2nd index
        for i in range(2, n):
            # calculate the cost to reach step i
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        
        # return the minimum cost to reach the top, which can be from either the last
        # or second to last step
        return min(dp[n - 1], dp[n - 2])

if __name__ == '__main__':
    s = Solution()
    print(s.minCostClimbingStairs([10,15,20]))
    print(s.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))