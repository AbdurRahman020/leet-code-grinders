class Solution:
    def isPowerOfFour1(self, n: int) -> bool:
        # Check if n is less than or equal to 0, as 0 and negative numbers are 
        # not powers of 4
        if n <= 0:
            return False
        
        # check if n is a power of 2 by bitwise AND with (n-1). If n is a power of 2,
        # it will have only one bit set. For powers of 4, this bit will always be at 
        # an odd position. For example, 4 (100), 16 (10000), 64 (1000000)
        if n & (n-1) != 0:
            return False
        
        # check if n % 3 equals 1. This is because all powers of 4 minus 1 are divisible 
        # by 3; For example, (4^1 - 1) = 3, (4^2 - 1) = 15, (4^3 - 1) = 63
        # so, if n % 3 is not equal to 1, it means n is not a power of 4
        if n % 3 != 1:
            return False
        
        # if none of the above conditions were met, n is a power of 4
        return True
    
    def isPowerOfFour2(self, n: int) -> bool:
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
        return self.isPowerOfFour2(n // 4)

if __name__ == '__main__':
    s = Solution()
    
    print(s.isPowerOfFour1(16))
    print(s.isPowerOfFour1(5))
    print(s.isPowerOfFour1(81))
    
    print(s.isPowerOfFour2(16))
    print(s.isPowerOfFour2(5))
    print(s.isPowerOfFour2(81))
    