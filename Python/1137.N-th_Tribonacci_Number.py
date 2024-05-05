from collections import defaultdict

class Solution:
    def tribonacci(self, n: int) -> int:
        # creating defaultdict for memoniztion values
        memo = defaultdict(int)
        # initailzing the base cases
        memo[0], memo[1], memo[2] = 0, 1, 1
        
        # helper function for recurrsion with memonization 
        def helper(n):
            # if num is already computed, return it from memo 
            if n in memo:
                return memo[n]
            # if num is not computed, compute it using recurrsion
            result = helper(n - 1) + helper(n - 2) + helper(n - 3)
            memo[n] = result
            return result
        # calling helper function for tribonacci num
        return helper(n)

if __name__ == '__main__':
    s = Solution()
    print(s.tribonacci(25))
    print(s.tribonacci(4))