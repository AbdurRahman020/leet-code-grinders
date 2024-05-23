class Solution:
    def findComplement(self, num: int) -> int:
        # calculate the bit mask to flip all the bits up to the leading 1 bit in num
        bit_mask = 2**num.bit_length() - 1
        # use XOR (^) operation between num and the bit mask to flip all the bits,
        # this will give the complement of num
        return (num ^ bit_mask)

if __name__ == '__main__':
    s = Solution()
    print(s.findComplement(5))
    print(s.findComplement(1))