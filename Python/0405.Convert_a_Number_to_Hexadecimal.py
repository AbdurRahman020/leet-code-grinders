class Solution:
    def toHex(self, num: int) -> str:
        # define the hex digit mapping (0-9, a-f)
        HEX_DIGITS = "0123456789abcdef"
        
        # edge case: If the number is 0, return "0"
        if num == 0:
            return "0"
       
        # stores the resulting hexadecimal representation
        hex_string = ""
        # keeps track of the number of 4-bit shifts (max 8 for 32-bit integer)
        shift_count = 0
        
        # convert the number to hexadecimal (handles both positive and negative numbers correctly)
        while num and shift_count < 8:
            # extract the last 4 bits (equivalent to num % 16)
            hex_string = HEX_DIGITS[num & 0xf] + hex_string  
            # right shift by 4 bits to process the next hex digit
            num >>= 4
            shift_count += 1
        
        return hex_string

if __name__ == '__main__':
    s = Solution()
    print(s.toHex(26))
    print(s.toHex(-1))
