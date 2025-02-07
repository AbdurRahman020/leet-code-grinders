from collections import defaultdict

class Solution:
    def tribonacci1(self, n: int) -> int:
        # creating defaultdict for memoniztion values
        memo = defaultdict(int)
        # initailzing the base cases
        memo[0], memo[1], memo[2] = 0, 1, 1
        
        # tribonacciHelper function for recurrsion with memonization 
        def tribonacciHelper(n):
            # if num is already computed, return it from memo 
            if n in memo:
                return memo[n]
            
            # if num is not computed, compute it using recurrsion
            tribonacci_num = tribonacciHelper(n - 1) + tribonacciHelper(n - 2) \
                + tribonacciHelper(n - 3)
            # store the computed value in memo for future reference
            memo[n] = tribonacci_num
            
            return tribonacci_num
        
        # calling the tribonacciHelper function to compute the tribonacci number
        return tribonacciHelper(n)
    
    def tribonacci2(self, n: int) -> int:
        # base case: if n is 0 or 1, return n as the Tribonacci number 
        if n <= 1:
            return n
        
        # base case: if n is 2, return 1 as the Tribonacci number
        elif n == 2:
            return 1
        
        # create a list (dp) to store the computed Tribonacci numbers up to n
        dp = [0] * (n + 1)
        # initialize the first three Tribonacci values
        dp[0], dp[1], dp[2] = 0, 1, 1

        # iterate from 3 to n to compute the Tribonacci numbers
        for i in range(3, n + 1):
            # each Tribonacci number is the sum of the three preceding numbers
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        
        # return the n-th Tribonacci number
        return dp[n]

if __name__ == '__main__':
    s = Solution()
    
    print(s.tribonacci1(25))
    print(s.tribonacci1(4))
    
    print(s.tribonacci2(25))
    print(s.tribonacci2(4))
