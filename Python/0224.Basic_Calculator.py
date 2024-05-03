class Solution:
    def calculate(self, s: str) -> int:
        # initialize variables: result for the final result, curr for current number, 
        # sign for current sign (+1 or -1), and stack for parentheses evaluation
        result, curr, sign, stack = 0, 0, 1, []
        
        # iterate through each character in the string
        for ch in s:
            # if the character is a digit, update curr
            if ch.isdigit():
                curr = int(ch)
            # if the character is a plus or minus sign, update result and reset curr
            elif ch in '+-':
                result += sign*curr
                # update sign based on the current operator
                sign = -1 if ch == '-' else 1
                curr = 0
            # if the character is an opening parenthesis, push current result 
            # and sign onto stack, reset result and sign
            elif ch == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            # if the character is a closing parenthesis, perform calculation within parentheses
            elif ch == ')':
                result += sign*curr
                # multiply the result by the sign on top of stack, then add the previous result on stack
                result *= stack.pop()
                result += stack.pop()
                curr = 0
        
        # return the final result after evaluating the entire string
        return result + sign*curr

if __name__ == '__main__':
    s = Solution()
    print(s.calculate("(1+(4+5+2)-3)+(6+8)"))
    print(s.calculate("1+1"))
    print(s.calculate("2-1+2"))