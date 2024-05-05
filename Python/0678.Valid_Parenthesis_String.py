class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        Checks if the given string is a valid string according to the defined rules.
        
        This method checks whether the given string is a valid string, where each character 
        can be one of the following:
        - '(' : Represents an opening bracket.
        - ')' : Represents a closing bracket.
        - '*' : Represents a stack that can be used as a substitute for either an opening 
               or a closing bracket.
        
        The rules for a valid string are as follows:
        1. Each opening bracket '(' must have a corresponding closing bracket ')'.
        2. Each closing bracket ')' must have a corresponding opening bracket '('.
        3. '*' can be used as a substitute for either an opening or a closing bracket.
        4. The '*' character cannot be used as a substitute for both opening and closing brackets.
        
        :param s: The string to be checked for validity.
        :type s: str
        
        :return: True if the string is valid, False otherwise.
        :rtype: bool
        """
        # lists to keep track of indices of opening brackets and stack
        bracket, stack = [], []
        
        # loop through each character in the string
        for i in range(len(s)):
            # if it's an opening bracket, add its index to the bracket list
            if s[i] == '(':
                bracket.append(i)
            # if it's a closing bracket
            elif s[i] == ')':
                # if there are opening brackets available, pop one
                if bracket:
                    bracket.pop()
                # if there are stack available, use one as a substitute for the closing bracket
                elif stack:
                    stack.pop()
                # if neither opening brackets nor stack are available, it's an invalid string
                else:
                    return False
            # if it's a stack, add its index to the stack list
            else:
                stack.append(i)
        
        # match remaining opening brackets with stack if possible
        while bracket and stack:
            # if an opening bracket's index is greater than a stack's index, it cannot be matched
            if bracket.pop() > stack.pop():
                return False
        
        # if there are no remaining opening brackets, the string is valid
        return not bracket

if __name__ == '__main__':
    s = Solution()
    print(s.checkValidString("(*))"))
    print(s.checkValidString("(*)"))
    print(s.checkValidString("(()*)(*"))