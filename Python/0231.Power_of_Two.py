class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # check if n is 0, 0 is not a power of 2
        if n == 0:
            return False
        
        # check if n is a power of 2 by bitwise AND with (n-1) 
        # if n is a power of 2, it will have only one bit set
        # bitwise AND of n and (n-1) will result in 0 in this case
        # example: if n = 16 (10000), (n-1) = 15 (01111) then n & (n-1) = 0
        if n & (n-1) == 0:
            return True
        # if n is not a power of 2, return False
        else:
            return False

if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfTwo(1))
    print(s.isPowerOfTwo(16))
    print(s.isPowerOfTwo(3))