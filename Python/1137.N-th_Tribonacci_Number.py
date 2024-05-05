from collections import defaultdict

class Solution:
    def tribonacci(self, n: int) -> int:
        """
        Calculates the nth Tribonacci number.
        
        The Tribonacci sequence is a sequence of numbers where each number is the sum of the three preceding ones.
        The first three numbers in the sequence are 0, 1, and 1.
        
        :param n: The index of the Tribonacci number to find.
        :type n: int
        
        :return: The nth Tribonacci number.
        :rtype: int
        """
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