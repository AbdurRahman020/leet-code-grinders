from typing import List

class Solution:
    def maxProfit1(self, prices: List[int]) -> int:
        # get the number of days (length of prices list)
        n = len(prices)
        
        # if there are no prices, no profit can be made
        if n == 0:
            return 0
        
        # initialize the dp array
        # dp[i][0]: maximum profit on day i when not holding stock
        # dp[i][1]: maximum profit on day i when holding stock
        dp = [[0] * 2 for _ in range(n)]
        
        # No stock on day 0, profit is 0
        dp[0][0] = 0
        # holding stock on day 0, profit is -prices[0]
        dp[0][1] = -prices[0]
        
        # iterate through each day starting from day 1
        for i in range(1, n):
            # calculate the maximum profit for day i when not holding stock
            # dp[i-1][0]: profit from not holding stock on previous day
            # dp[i-1][1] + prices[i]: profit from selling stock today
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            
            # calculate the maximum profit for day i when holding stock
            # dp[i-1][1]: profit from holding stock on previous day
            # dp[i-1][0] - prices[i]: profit from buying stock today
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        
        # the maximum profit will be the max profit on the last day when not holding stock
        return max(dp[-1][0], 0)
    
    def maxProfit2(self, prices: List[int]) -> int:
        # get the number of days (length of prices list)
        n = len(prices)
        
        # if there are no prices, no profit can be made
        if n == 0:
            return 0
        
        # initialize profit to zero
        profit = 0
        
        # iterate through the prices starting from the second day
        for i in range(1, n):
            # if the price today is greater than the price yesterday
            if prices[i] > prices[i-1]:
                # accumulate profit from buying yesterday and selling today
                profit += prices[i] - prices[i-1]
        
        # return the total calculated profit
        return profit
        
        # one-liner code
        # return sum(max(b - a, 0) for a, b in itertools.pairwise(prices))

if __name__ == '__main__':
    s = Solution()
    
    print(s.maxProfit1([7,1,5,3,6,4]))
    print(s.maxProfit1([1,2,3,4,5]))
    print(s.maxProfit1([7,6,4,3,1]))
    
    print(s.maxProfit2([7,1,5,3,6,4]))
    print(s.maxProfit2([1,2,3,4,5]))
    print(s.maxProfit2([7,6,4,3,1]))
