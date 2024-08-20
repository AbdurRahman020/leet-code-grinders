class Solution:
    def removeStars(self, input_str: str) -> str:
        # initialize an empty list to use as a stack
        stack = []
        
        # iterate over each character in the input string
        for char in input_str:
            # if the character is a star ('*'), remove the top element from the stack
            if char == '*':
                # pop the last character added to the stack (if stack is not empty)
                if stack:
                    stack.pop()
            else:
                # if the character is not a star, push it onto the stack
                stack.append(char)
        
        # join all characters in the stack to form the final result string
        return ''.join(stack)

if __name__ == '__main__':
    s = Solution()
    print(s.removeStars("leet**cod*e"))
    print(s.removeStars("erase*****"))