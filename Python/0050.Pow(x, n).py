class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n, x = -n, 1/x
        if n == 0:
            return 1
        if n == 1:
            return x
        
        less_pow = self.myPow(x, n//2)
        
        if n % 2 == 0:
            return less_pow * less_pow
        else:
            return less_pow * less_pow * x

if __name__ == '__main__':
    s = Solution()
    print(s.myPow(2.00000, 10))
    print(s.myPow(2.10000, 3))
    print(s.myPow(2.00000, -2))