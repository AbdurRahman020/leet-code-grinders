class Solution:
    def perfect_num(self, p: int) -> int:
        return (1 << (p - 1)) * ((1 << p) - 1)
    
    def checkPerfectNumber(self, num: int) -> bool:
        primes = [2, 3, 5, 7, 13, 17, 19, 31]
        
        for prime in primes:
            if self.perfect_num(prime) == num:
                return True
        
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.checkPerfectNumber(7))
    print(s.checkPerfectNumber(28))
