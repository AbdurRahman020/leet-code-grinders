class Solution:
    def toLowerCase(self, s: str) -> str:
        # initialize an empty string to store the result with all characters in lowercase
        lower_case_str = ''
        
        # iterate over each character in the input string
        for char in s:
            # get the ASCII value of the current character
            ascii_val = ord(char)
            
            # check if the ASCII value corresponds to an uppercase letter
            if 65 <= ascii_val <= 90:
                # convert the uppercase letter to lowercase by adding 32 to its ASCII value,
                # append the converted character to the result string
                lower_case_str += chr(ascii_val + 32)
            else:
                # if the character is not an uppercase letter, simply append it to the 
                # result string as is
                lower_case_str += char
        
        # Return the resulting string with all characters converted to lowercase
        return lower_case_str

if __name__ == '__main__':
    s = Solution()
    print(s.toLowerCase("Hello"))
    print(s.toLowerCase("LOVELY"))
    print(s.toLowerCase("here"))