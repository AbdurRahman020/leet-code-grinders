from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
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
    print(s.maxProfit([7,1,5,3,6,4]))
    print(s.maxProfit([1,2,3,4,5]))
    print(s.maxProfit([7,6,4,3,1]))