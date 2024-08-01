class Solution:
    def myPow(self, x: float, n: int) -> float:
        # if the exponent n is negative, invert the base x and make n positive
        if n < 0:
            n, x = -n, 1/x
        
        # base case 1: any number raised to the power of 0 is 1
        if n == 0:
            return 1
        
        # base case 2: any number raised to the power of 1 is the number itself
        if n == 1:
            return x
        
        # recursive case: compute the power of x for n // 2, this step reduces 
        # the problem size for faster computation
        less_pow = self.myPow(x, n // 2)
        
        # if n is even, the result is (x^(n/2))^2
        if n % 2 == 0:
            return less_pow * less_pow
        # if n is odd, the result is (x^(n//2))^2 * x, because we need one more 
        # multiplication by x
        else:
            return less_pow * less_pow * x

if __name__ == '__main__':
    s = Solution()
    print(s.myPow(2.00000, 10))
    print(s.myPow(2.10000, 3))
    print(s.myPow(2.00000, -2))