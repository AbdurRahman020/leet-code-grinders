class Solution(object):
    def canWinNim(self, n: int) -> bool:
        if n % 4 == 0:
            return False
        else:
            return True 

if __name__ == '__main__':
    s = Solution()
    print(s.canWinNim(4))
    print(s.canWinNim(3))
    print(s.canWinNim(1))