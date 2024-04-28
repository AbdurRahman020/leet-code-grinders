class Solution(object):
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        while n > 1:
            if n%2 == 0:
                n = n//2
            elif n%3 == 0:
                n = n//3
            elif n%5 == 0:
                n = n//5
            else:
                return False
        if n == 1: 
            return True
        
if __name__ == '__main__':
    s = Solution()
    print(s.isUgly(6))
    print(s.isUgly(14))
    print(s.isUgly(20))
    print(s.isUgly(1))