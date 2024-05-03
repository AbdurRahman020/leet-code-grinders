import math

class Solution:
    def calculate(self, s: str) -> int:
        # initialize stack, num, and sign
        stack, num, sign = [], 0, '+'
        
        # iterate through the string with an extra '+' at the end
        for ch in s + '+':
            # if the character is a digit, update num
            if ch.isdigit():
                num = 10*num + int(ch)
            # if the character is an operator, perform corresponding operation
            elif ch in '+-*/':
                # if the previous operator was '+', push num onto stack
                if sign == '+':
                    stack.append(num)
                # if the previous operator was '*', perform multiplication with top of stack and num
                elif sign == '*':
                    stack.append(stack.pop()*num)
                # if the previous operator was '-', push negative of num onto stack
                elif sign == '-':
                    stack.append(-num)
                # if the previous operator was '/', perform integer division with top of stack and num
                elif sign == '/':
                    stack.append(math.trunc(stack.pop()/num))
                # update sign and reset num
                sign = ch
                num = 0
        
        # return the sum of the stack elements, which represent the final result 
        return sum(stack)

if __name__ == '__main__':
    s = Solution()
    print(s.calculate("3+5/2"))
    print(s.calculate("3/2"))
    print(s.calculate("3+2*2"))