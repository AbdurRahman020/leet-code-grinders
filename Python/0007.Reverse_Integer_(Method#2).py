class Solution(object):
    def reverse(self, x: int) -> int:
        """
        Reverses the digits of an integer.

        :param x: The integer to be reversed.
        :type x: int
        
        :return: The reversed integer.
        :rtype: int
        """
        # initialize a variable to store the reversed integer
        int_reversed = 0
        # check if the input number is non-negative
        if x >= 0:
            # if non-negative, reverse the digits directly
            int_reversed = int(str(x)[::-1])
        else:
            # if negative, remove the minus sign, reverse the digits, then add back the minus sign
            int_reversed = int(str(x)[1:][::-1])*-1
        
        # check for overflow conditions
        if int_reversed < -2**31 or int_reversed > 2**31 - 1:
            return 0
        
        # check if the input number is exactly -2**31 and the reversed integer is less than -2**31
        if x == -2**31 and int_reversed < -2**31:
            return 0
        
        # return the reversed integer
        return int_reversed

if __name__ == '__main__':
    s = Solution()
    print(s.reverse(-123))
    print(s.reverse(1534236469))
    print(s.reverse(120))