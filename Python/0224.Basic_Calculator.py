class Solution:
    def calculate(self, s: str) -> int:
        result, curr, sign, stack = 0, 0, 1, []
        
        for ch in s:
            if ch.isdigit():
                curr = int(ch)
            elif ch in '+-':
                result += sign*curr
                sign = -1 if ch == '-' else 1
                curr = 0
            elif ch == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif ch == ')':
                result += sign*curr
                result *= stack.pop()
                result += stack.pop()
                curr = 0
                
        return result + sign*curr

if __name__ == '__main__':
    s = Solution()
    print(s.calculate("(1+(4+5+2)-3)+(6+8)"))
    print(s.calculate("1+1"))
    print(s.calculate("2-1+2"))