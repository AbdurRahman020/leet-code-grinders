class Solution:
    def checkValidString(self, s: str) -> bool:
        bracket, star = [], []
        
        for i in range(len(s)):
            if s[i] == '(':
                bracket.append(i)
            elif s[i] == ')':
                if bracket:
                    bracket.pop()
                elif star:
                    star.pop()
                else:
                    return False
            else:
                star.append(i)
        
        while bracket and star:
            if bracket.pop() > star.pop():
                return False
            
        return not bracket

if __name__ == '__main__':
    s = Solution()
    print(s.checkValidString("(*))"))
    print(s.checkValidString("(*)"))
    print(s.checkValidString("(()*)(*"))