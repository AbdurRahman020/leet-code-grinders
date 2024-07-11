class Solution:
    def reverseParentheses(self, s: str) -> str:
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

if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseParentheses("(abcd)"))
    print(solution.reverseParentheses("(u(love)i)"))
    print(solution.reverseParentheses("(ed(et(oc))el)"))