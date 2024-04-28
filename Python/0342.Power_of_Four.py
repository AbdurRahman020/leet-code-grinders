class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and n & (n-1) == 0 and n % 3 == 1

if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfFour(16))
    print(s.isPowerOfFour(5))
    print(s.isPowerOfFour(81))