class Solution:
    def decodeString(self, s: str) -> str:
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
    print(s.decodeString("3[a]2[bc]"))
    print(s.decodeString("3[a2[c]]"))
    print(s.decodeString("2[abc]3[cd]ef"))