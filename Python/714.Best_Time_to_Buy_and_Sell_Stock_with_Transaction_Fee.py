from typing import List
from math import inf

class Solution:
    def maxProfit1(self, prices: List[int], fee: int) -> int:
        # get the number of days
        n = len(prices)
        
        # initialize a dp table with dimensions (n+1) x 2:
        #   dp[i][0] will store the maximum profit on day i when not holding a stock
        #   dp[i][1] will store the maximum profit on day i when holding a stock
        dp = [[0] * 2 for _ in range(n + 1)]
        
        # base case: no profit on day 0 without holding stock
        dp[0][0] = 0         
        # base case: impossible state, can't hold stock without buying
        dp[0][1] = -inf

        # iterate through each day's price
        for i, p in enumerate(prices):
            # calculate the maximum profit for not holding a stock on day i+1
            #   option 1: stay in the same state as the previous day (not holding stock)
            #   option 2: sell the stock we were holding (if we had one) and subtract the transaction fee
            dp[i + 1][0] = max(dp[i][0], dp[i][1] + prices[i] - fee)
            
            # calculate the maximum profit for holding a stock on day i+1
            #   option 1: stay in the same state as the previous day (holding stock)
            #   option 2: buy a stock today (subtract today's price from the profit)
            dp[i + 1][1] = max(dp[i][1], dp[i][0] - prices[i])

        # the answer will be the maximum profit on the last day when not holding any stock
        return dp[n][0]
    
    def maxProfit2(self, prices: List[int], fee: int) -> int:
        # initialize dp0 and dp1
        #   dp0 represents the maximum profit when not holding a stock
        #   dp1 represents the maximum profit when holding a stock
        dp0, dp1 = 0, -inf
        
        # iterate through each day's price
        for _, p in enumerate(prices):
            # update dp0: maximum profit without holding stock
            #   option 1: remain in the same state (not holding stock)
            #   option 2: sell the stock we were holding (if we had one) and deduct the transaction fee
            dp0, dp1 = max(dp0, dp1 + p - fee), max(dp1, dp0 - p)
        
        # return the maximum profit when not holding any stock at the end
        return dp0

if __name__ == '__main__':
    s = Solution()
    
    print(s.maxProfit1([1,3,2,8,4,9], 2))
    print(s.maxProfit1([1,3,7,5,10,3], 3))
    
    print(s.maxProfit2([1,3,2,8,4,9], 2))
    print(s.maxProfit2([1,3,7,5,10,3], 3))
