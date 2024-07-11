import re

class Solution:
    def reverseParentheses(self, s: str) -> str:
        # regular expression pattern to match parentheses with lowercase letters inside
        pattern = "\\(([a-z]*?)\\)"

        # function to reverse the substring inside parentheses
        def reverse_inside_parentheses(match):
            substring_inside_parentheses = match.group(1)
            return substring_inside_parentheses[::-1]

        # check if there are parentheses in the string
        if "(" in s:
            # recursively replace substrings inside parentheses with their reversed versions
            return self.reverseParentheses(re.sub(pattern, reverse_inside_parentheses, s))
        else:
            # no parentheses found, return the original string
            return s

if __name__ == '__main__':
    s = Solution()
    print(s.reverseParentheses("(abcd)"))
    print(s.reverseParentheses("(u(love)i)"))
    print(s.reverseParentheses("(ed(et(oc))el)"))