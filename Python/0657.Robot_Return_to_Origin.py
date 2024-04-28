class Solution:
    def judgeCircle(self, moves: str) -> bool:
        y_movment = moves.count('U') - moves.count('D')
        x_movment = moves.count('R') - moves.count('L')
        return x_movment == 0 and y_movment == 0

if __name__ == '__main__':
    s = Solution()
    print(s.judgeCircle('RRDD'))
    print(s.judgeCircle('LL'))
    print(s.judgeCircle('LDRRUDLU'))