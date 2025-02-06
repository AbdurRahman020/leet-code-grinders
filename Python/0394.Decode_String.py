class Solution:
    def decodeString1(self, s: str) -> str:
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
    
    def decodeString2(self, s: str) -> str:
        # a helper function to perform the decoding
        def decode(i, num_str, pos):
            # base case: if the index is out of bounds, return an empty string
            if i >= len(s):
                return ''
            
            # if we encounter a closing bracket, record its position and return an empty string
            if s[i] == ']':
                pos[0] = i
                return ''
            
            # if we encounter an opening bracket, decode the substring within the brackets
            # multiply the decoded substring by the number represented by num_str and 
            # concatenate with the result of decoding the rest of the string after the bracket
            if s[i] == '[':
                return int(num_str) * decode(i + 1, '', pos) + decode(pos[0] + 1, '', pos)
            
            # if the current character is a digit, accumulate it to form the number
            if s[i].isdigit():
                return decode(i + 1, num_str + s[i], pos)
            # if the current character is a letter, include it in the result and continue decoding
            else:
                return s[i] + decode(i + 1, num_str, pos)
        
        # initialize the position list with a single element 0
        pos = [0]
        
        # start decoding from the first index, with an empty number string, and position list
        return decode(0, '', pos)

if __name__ == '__main__':
    s = Solution()
    
    print(s.decodeString1("3[a]2[bc]"))
    print(s.decodeString1("3[a2[c]]"))
    print(s.decodeString1("2[abc]3[cd]ef"))
    
    print(s.decodeString2("3[a]2[bc]"))
    print(s.decodeString2("3[a2[c]]"))
    print(s.decodeString2("2[abc]3[cd]ef"))
