class Solution(object):
    def divide(self, dividend: int, divisor: int) -> int:
        # check if dividend is zero
        if dividend == 0:
            return 0
        # check if divisor is zero
        if divisor == 0:
            return RuntimeError("Divison by ZERO")
        # special case handling: dividend is the minimum integer and divisor is -1
        if dividend == -2**31 and divisor == -1:
            return (2**31)-1
        # determine if the result should be positive or negative
        if (dividend < 0 and divisor < 0) or ((dividend > 0 and divisor > 0)):
            sign_pos = True
        else:
            sign_pos = False
        
        # convert both dividend and divisor to positive numbers
        dividend, divisor = abs(dividend), abs(divisor)
        
        # initialize the quotient
        quotient = 0
        # iterate from the highest bit to the lowest bit of the dividend
        for i in reversed(range(dividend.bit_length() - divisor.bit_length() + 1)):
            # check if the current divisor can be subtracted from the current dividend
            if dividend >> i >= divisor:
                # subtract the divisor from the dividend
                dividend -= divisor << i
                # update the quotient by setting the corresponding bit to 1
                quotient |= 1 << i
        
        # return the quotient with the correct sign
        return quotient if sign_pos else -quotient 
            
if __name__ == '__main__':
    s = Solution()
    print(s.divide(1, 0))
    print(s.divide(7, -3))
    print(s.divide(2**31-1, -2**20))