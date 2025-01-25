from functools import lru_cache

class Solution:
    @lru_cache(None)
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)

if __name__ == '__main__':
    s = Solution()
    print(s.fib(2))
    print(s.fib(3))
    print(s.fib(4))
