import math

class Solution:
    def calculate(self, s: str) -> int:
        stack, num, sign = [], 0, '+'
        
        for ch in s + '+':
            if ch.isdigit():
                num = 10*num + int(ch)
            elif ch in '+-*/':
                if sign == '+':
                    stack.append(num)
                elif sign == '*':
                    stack.append(stack.pop()*num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '/':
                    stack.append(math.trunc(stack.pop()/num))
                sign = ch
                num = 0
                
        return sum(stack)

if __name__ == '__main__':
    s = Solution()
    print(s.calculate("3+5/2"))
    print(s.calculate("3/2"))
    print(s.calculate("3+2*2"))