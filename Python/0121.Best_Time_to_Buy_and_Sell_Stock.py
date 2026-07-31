from typing import List
from math import inf


class Solution:
    def maxProfit1(self, prices: List[int]) -> int:
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

    def maxProfit2(self, prices: List[int]) -> int:
        n = len(prices)
        # initialize max_profit to 0 and min_price to the first price in the list
        max_profit, min_price = 0, prices[0]

        # iterate through the prices list starting from the second element
        for i in range(1, n):
            # calculate the potential profit at the current price and update max_profit if it's higher
            max_profit = max(max_profit, prices[i] - min_price)
            # update min_price to the lowest price seen so far
            min_price = min(min_price, prices[i])

        # return the maximum profit found
        return max_profit


if __name__ == '__main__':
    s = Solution()

    print(s.maxProfit1([7, 1, 5, 3, 6, 4]))
    print(s.maxProfit1([7, 6, 4, 3, 1]))

    print(s.maxProfit2([7, 1, 5, 3, 6, 4]))
    print(s.maxProfit2([7, 6, 4, 3, 1]))
