class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        # initialize the counter for the number of flips needed
        flips = 0
        
        # iterate through each bit position from 0 to 31
        for i in range(32):
            bit_a = (a>>i) & 1  # extract the i-th bit from number a
            bit_b = (b>>i) & 1  # extract the i-th bit from number b
            bit_c = (c>>i) & 1  # extract the i-th bit from number c
            
            # check if the i-th bit in c is 0
            if bit_c == 0:
                # if bit_c is 0, both bit_a and bit_b must be 0 to satisfy the
                # condition without flipping 
                # hence, count flips needed to make both bit_a and bit_b 0
                flips += (bit_a + bit_b)
            else:
                # if bit_c is 1, at least one of bit_a or bit_b must be 1
                # if both are 0, we need to flip at least one of them to make the result 1
                if bit_a == 0 and bit_b == 0:
                    flips += 1
        
        # return the total number of flips needed
        return flips         
        
        # one liner approch
        # return (c := (a | b) ^ c).bit_count() + (a & b & c).bit_count()

if __name__ == '__main__':
    s = Solution()
    print(s.minFlips(2, 6, 5))
    print(s.minFlips(4, 2, 7))
    print(s.minFlips(1, 2, 3))