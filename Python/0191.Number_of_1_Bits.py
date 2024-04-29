class Solution:
    def hammingWeight(self, n: int) -> int:
        # initialize a variable to count the number of set bits (bits with value 1)
        count = 0
        # iterate through each bit position from 0 to 31 (assuming 32-bit integer)
        for i in range(32):
            # right shift the number n by i positions and perform bitwise AND with 1
            # if the result is 1, it means the bit at position i is set (i.e., it's a 1)
            if (n>>i) & 1:
                # increment the count if the bit is set
                count += 1
        # return the total count of set bits
        return count

if __name__ == '__main__':
    s = Solution()
    print(s.hammingWeight(2147483645))
    print(s.hammingWeight(128))
    print(s.hammingWeight(11))