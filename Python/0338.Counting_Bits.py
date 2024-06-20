class Solution:
    def countBits(self, n: int) -> list[int]:
        # initialize an empty list to store the count of bits for each number from 0 to n
        counter = [0]
        
        # loop through each number from 1 to n
        for i in range(1, n+1):
            # to count the number of 1s in the binary representation of `i`, we use:
            # counter[i >> 1] + i % 2
            #
            # explanation: i >> 1 shifts the bits of i to the right by 1 position, which effectively
            # divides i by 2 and floors the result. This gives us the count of 1s in
            # the binary representation of i // 2
            #
            # i % 2 gives the least significant bit of i, which is either 0 or 1
            #
            # therefore, counter[i >> 1] + i % 2 gives us the count of 1s in the binary
            # representation of i and we append this count to the `counter` list
            counter.append(counter[i>>1] + i%2)
        
        # return the list containing the count of bits for each number from 0 to n
        return counter

if __name__ == '__main__':
    s = Solution()
    print(s.countBits(5))
    print(s.countBits(9))
    print(s.countBits(2))