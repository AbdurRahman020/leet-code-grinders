class Solution:
    def numTilings(self, n: int) -> int:
        # base cases for n less than 3
        if n < 3:
            # if n is 1, we can only fill it in one way (1 domino), and for n=2 
            # (2 dominos), we can fill it in two ways
            return n
        
        # initialize a list to store the number of ways to tile the board for 
        # each length up to n
        dp = [0] * n
        # base cases for dp array:
        # dp[0] corresponds to n=1: 1 way to fill
        # dp[1] corresponds to n=2: 2 ways to fill (2 vertical or 1 horizontal)
        # dp[2] corresponds to n=3: 5 ways to fill (various combinations of 
        # horizontal and vertical tiles)
        dp[0], dp[1], dp[2] = 1, 2, 5
        
        # loop through the dp array from index 3 to n-1
        for i in range(3, len(dp)):
            # calculate the number of ways to tile a board of length i
            # dp[i-1] * 2 accounts for adding a vertical tile to the previous 
            # configurations (2 ways to place the tile)
            # dp[i-3] accounts for placing a horizontal tile that covers 3 
            # squares (thus leaving dp[i-3])
            dp[i] = (dp[i-1] * 2 + dp[i-3]) % (10**9 + 7)  # modulo to prevent overflow
        
        # return the number of ways to fill a board of length n
        return dp[n-1]

if __name__ == '__main__':
    s = Solution()
    print(s.numTilings(3))
    print(s.numTilings(1))