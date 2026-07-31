class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # initialize variables
        result, total, i, j = [], 0, len(a) - 1, len(b) - 1

        # loop until all digits are processed and there's no carry left
        while i >= 0 or j >= 0 or total:
            # if there are still digits left in string 'a'
            if i >= 0:
                # add the integer value of the current digit of 'a' to 'total'
                total += int(a[i])
                # move to the next digit
                i -= 1

            # if there are still digits left in string 'b'
            if j >= 0:
                # add the integer value of the current digit of 'b' to 'total'
                total += int(b[j])
                # move to the next digit
                j -= 1

            # append the least significant bit (total % 2) of 'total' to the result
            result.append(str(total % 2))
            # update 'total' by dividing it by 2 (shift right in binary terms)
            total //= 2

        # return the result list as a string, reversing it since we built it backwards
        return ''.join(reversed(result))

        # method 2
        # return bin(int(a,2) + int(b,2))[2:]


if __name__ == '__main__':
    s = Solution()
    print(s.addBinary("11", "1"))
    print(s.addBinary("1010", "1011"))
