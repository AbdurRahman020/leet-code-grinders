class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # check if n is less than or equal to 0, as 0 and negative numbers are not 
        # powers of 4
        if n <= 0:
            return False
        
        # check if n is equal to 1. 1 is considered as a power of 4
        if n == 1:
            return True
        
        # check if n is divisible by 4. If n is not divisible by 4, then it cannot
        # be a power of 4, as powers of 4 will always be divisible by 4
        if n % 4 != 0:
            return False
        
        # if n is divisible by 4, recursively call the function with n divided by 4
        # this continues the process of dividing n by 4 until either n becomes 1 
        # (which is a power of 4) or it encounters a number not divisible by 4, 
        # in which case it returns False
        return self.isPowerOfFour(n // 4)

if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfFour(16))
    print(s.isPowerOfFour(5))
    print(s.isPowerOfFour(81))