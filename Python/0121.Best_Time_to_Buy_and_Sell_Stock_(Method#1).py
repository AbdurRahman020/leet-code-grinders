from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # get the number of days (length of prices list)
        n = len(prices)
        
        # check if there are no prices
        if n == 0:
            # if no prices, return 0 profit
            return 0
        
        # initialize a 2D list dp with n rows and 2 columns
        dp = [[0] * 2 for _ in range(n)]
        # set the first day's price as the initial minimum price
        dp[0][0] = prices[0]
        
        # iterate through the prices starting from the second day
        for i in range(1, n):
            # calculate the minimum price up to the current day
            min_price = min(dp[i-1][0], prices[i])
            # calculate the maximum profit up to the current day
            max_profit = max(dp[i-1][1], prices[i] - dp[i-1][0])
            
            # update the dp array for the current day
            dp[i] =[min_price,max_profit]
        
        # return the maximum profit on the last day
        return dp[n-1][1]

if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))
    print(s.maxProfit([7,6,4,3,1]))