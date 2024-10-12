from typing import List
from math import inf

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # initialize min_price to infinity and max_profit to 0
        min_price, max_profit = inf, 0

        # iterate through each price in the prices list
        for price in prices:
            # check if the current price is less than the recorded minimum price
            if price < min_price:
                # update min_price to the current price if it's lower
                min_price = price
            # check if the current profit is greater than the recorded max_profit
            elif max_profit < price - min_price:
                # update max_profit to the new maximum profit
                max_profit = price - min_price
        
        # return the maximum profit calculated
        return max_profit

if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))
    print(s.maxProfit([7,6,4,3,1]))