class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # count the number of 'U' (up) moves and 'D' (down) moves
        y_movment = moves.count('U') - moves.count('D')
        # count the number of 'R' (right) moves and 'L' (left) moves
        x_movment = moves.count('R') - moves.count('L')
        
        # to return True, the movements should cancel out both horizontally and vertically
        return x_movment == 0 and y_movment == 0

if __name__ == '__main__':
    s = Solution()
    print(s.judgeCircle('RRDD'))
    print(s.judgeCircle('LL'))
    print(s.judgeCircle('LDRRUDLU'))