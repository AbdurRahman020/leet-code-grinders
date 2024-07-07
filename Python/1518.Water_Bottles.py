class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # initialize variables to track total bottles drunk and empty bottles left
        total_drunk = 0
        empty = 0
        
        # continue drinking until there are no more full bottles left
        while numBottles > 0:
            # drink all the full bottles
            total_drunk += numBottles
            # add the empty bottles to the collection of empty bottles
            empty += numBottles
            # calculate how many new full bottles can be obtained by exchanging the empty bottles
            numBottles = empty // numExchange
            # calculate how many empty bottles are left after exchanging
            empty %= numExchange
        
        # return the total number of bottles drunk
        return total_drunk

if __name__ == '__main__':
    s = Solution()
    print(s.numWaterBottles(9, 3))
    print(s.numWaterBottles(15, 4))