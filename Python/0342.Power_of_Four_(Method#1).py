class Solution:
    def isPowerOfFour(self, n: int) -> bool:
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

if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfFour(16))
    print(s.isPowerOfFour(5))
    print(s.isPowerOfFour(81))