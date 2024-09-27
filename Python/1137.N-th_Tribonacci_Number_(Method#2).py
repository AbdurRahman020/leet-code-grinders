from collections import defaultdict

class Solution:
    def tribonacci(self, n: int) -> int:
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

if __name__ == '__main__':
    s = Solution()
    print(s.tribonacci(25))
    print(s.tribonacci(4))