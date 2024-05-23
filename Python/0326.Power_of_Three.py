class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # check if n is 0. Zero is not a power of three
        if n == 0:
            return False
        
        # check if n is 1. One is considered as a power of three
        if n == 1:
            return True
        
        # check if n is divisible by 3. If n is not divisible by 3,
        # then it cannot be a power of three, as powers of three will always 
        # be divisible by 3
        if n % 3 != 0:
            return False
        
        # if n is divisible by 3, recursively call the function with n divided by 3
        # this continues the process of dividing n by 3 until either n becomes 1
        # (which is a power of three) or it encounters a number not divisible by 3, 
        # in which case it returns False.
        return self.isPowerOfThree(n // 3)

if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfThree(27))
    print(s.isPowerOfThree(0))
    print(s.isPowerOfThree(-1))