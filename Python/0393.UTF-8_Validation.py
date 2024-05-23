from typing import List

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        # initialize a count to keep track of the number of expected bytes
        count = 0
        
        # iterate through each byte in the data
        for byte in data:
            # if count is 0, it means we are at the beginning of a new character
            if count == 0:
                # check if the byte represents a 2-byte character
                if byte >> 5 == 0b110:
                    count = 1
                # check if the byte represents a 3-byte character
                elif byte >> 4 == 0b1110:
                    count = 2
                # check if the byte represents a 4-byte character
                elif byte >> 3 == 0b11110:
                    count = 3
                # if the byte doesn't match any of the UTF-8 starting byte patterns,
                # it's either a single-byte character or an invalid byte, so we check
                # if the most significant bit is 0
                elif byte >> 7 != 0b0:
                    return False
            else:
                # for bytes following the starting byte of a multi-byte character,
                # we expect the two most significant bits to be 10
                if byte >> 6 != 0b10:
                    return False
                # decrease the count as we consume bytes of the multi-byte character
                count -= 1
        
        # if count is 0 at the end, it means all multi-byte characters were properly
        # terminated, and there were no incomplete characters
        return count == 0

if __name__ == '__main__':
    s = Solution()
    print(s.validUtf8([197,130,1]))
    print(s.validUtf8([235,140,4]))