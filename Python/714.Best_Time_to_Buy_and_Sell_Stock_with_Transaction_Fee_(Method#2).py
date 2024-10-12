from typing import List
from math import inf

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
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
    print(s.maxProfit([1,3,2,8,4,9], 2))
    print(s.maxProfit([1,3,7,5,10,3], 3))