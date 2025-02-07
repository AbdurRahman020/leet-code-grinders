import re

class Solution:
    def reverseParentheses1(self, s: str) -> str:
        # initialize stack with an empty string
        stack = ['']
        
        # iterate through each character in the input string 's'
        for ch in s:
            if ch == '(':
                # if current character is '(', push an empty string to start collecting characters inside parentheses
                stack.append('')
            elif ch == ')':
                # if current character is ')', pop the last string from stack to reverse
                substring_to_reverse = stack.pop()
                # reverse the substring
                reversed_substring = substring_to_reverse[::-1]
                # append the reversed substring to the string on top of the stack
                stack[-1] += reversed_substring
            else:
                # if current character is neither, append it to the current string on top of the stack
                stack[-1] += ch
        
        # return the final result after all operations, which is the string after processing all parentheses
        return stack.pop()
    
    def reverseParentheses2(self, s: str) -> str:
        # regular expression pattern to match parentheses with lowercase letters inside
        pattern = "\\(([a-z]*?)\\)"
        
        # function to reverse the substring inside parentheses
        def reverse_inside_parentheses(match):
            substring_inside_parentheses = match.group(1)
            return substring_inside_parentheses[::-1]
        
        # check if there are parentheses in the string
        if "(" in s:
            # recursively replace substrings inside parentheses with their reversed versions
            return self.reverseParentheses2(re.sub(pattern, reverse_inside_parentheses, s))
        else:
            # no parentheses found, return the original string
            return s

if __name__ == '__main__':
    solution = Solution()
    
    print(solution.reverseParentheses1("(abcd)"))
    print(solution.reverseParentheses1("(u(love)i)"))
    print(solution.reverseParentheses1("(ed(et(oc))el)"))
    
    print(solution.reverseParentheses2("(abcd)"))
    print(solution.reverseParentheses2("(u(love)i)"))
    print(solution.reverseParentheses2("(ed(et(oc))el)"))
