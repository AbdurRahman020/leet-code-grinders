class Solution:
    def decodeString(self, s: str) -> str:
        # initialize an empty string to build the decoded result
        decoded_str = ''
        # initialize a variable to store the current repeat count
        repeat_count = 0
        # initialize a stack to keep track of previous strings and repeat counts
        stack = []
        
        # iterate through each character in the input string
        for char in s:
            # if the character is a digit, update the repeat count
            if char.isdigit():
                repeat_count = repeat_count * 10 + int(char)
            # if the character is an opening bracket, push the current decoded string
            # and repeat count onto the stack, then reset them for the new segment
            elif char == '[':
                stack.append(decoded_str)
                stack.append(repeat_count)
                decoded_str = ''
                repeat_count = 0
            # if the character is a closing bracket, pop the repeat count and the
            # previous string from the stack, and append the current decoded string
            # repeated by the count to the previous string
            elif char == ']':
                count = stack.pop()
                previous_str = stack.pop()
                decoded_str = previous_str + count * decoded_str
            # if the character is a letter, append it to the current decoded string
            else:
                decoded_str += char
        
        # return the final decoded string
        return decoded_str

if __name__ == '__main__':
    s = Solution()
    print(s.decodeString("3[a]2[bc]"))
    print(s.decodeString("3[a2[c]]"))
    print(s.decodeString("2[abc]3[cd]ef"))