class Solution:
    def reverse1(self, x: int) -> int:
        # initialize an empty string to store the reversed integer as a string
        int_reversed = ''
        # initialize a variable to track the sign of the number
        sign = 1

        # iterate through each character of the input integer converted to a string
        for i in str(x):
            # check if the character is a minus sign
            if i == '-':
                # if it is, update the sign variable accordingly
                sign = -1
            else:
                # if it's not a minus sign, add the character to the
                # int_reversed string
                int_reversed += i

        # convert the int_reversed string back to an integer, reverse it, and
        # adjust its sign
        int_reversed = sign*int(int_reversed[::-1])
        # check for overflow conditions
        if int_reversed > 2**31 - 1 or int_reversed < -2**31:
            return 0

        # return the reversed integer
        return int_reversed

    def reverse2(self, x: int) -> int:
        # initialize a variable to store the reversed integer
        int_reversed = 0

        # check if the input number is non-negative
        if x >= 0:
            # if non-negative, reverse the digits directly
            int_reversed = int(str(x)[::-1])
        else:
            # if negative, remove the minus sign, reverse the digits, then add
            # back the minus sign
            int_reversed = int(str(x)[1:][::-1])*-1

        # check for overflow conditions
        if int_reversed < -2**31 or int_reversed > 2**31 - 1:
            return 0

        # check if the input number is exactly -2**31 and the reversed integer
        # is less than -2**31
        if x == -2**31 and int_reversed < -2**31:
            return 0

        # return the reversed integer
        return int_reversed


if __name__ == '__main__':
    s = Solution()

    print(s.reverse1(-123))
    print(s.reverse1(1534236469))
    print(s.reverse1(120))

    print(s.reverse2(-123))
    print(s.reverse2(1534236469))
    print(s.reverse2(120))
