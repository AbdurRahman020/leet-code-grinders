class Solution:
    def bitwiseComplement(self, n: int) -> int:
        # check if n is 0, if so, its complement is 1
        if n == 0:
            return 1
        # calculate the bit mask to flip all the bits up to the leading 1 bit in n
        bit_mask = 2**n.bit_length() - 1
        
        # use XOR (^) operation between n and the bit mask to flip all the bits,
        # this will give the complement of n
        return (n ^ bit_mask)

if __name__ == '__main__':
    s = Solution()
    print(s.bitwiseComplement(5))
    print(s.bitwiseComplement(10))
    print(s.bitwiseComplement(7))