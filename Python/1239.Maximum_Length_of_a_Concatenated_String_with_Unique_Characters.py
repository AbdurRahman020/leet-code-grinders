from typing import List

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # number of strings in the input list
        n = len(arr)
        
        # function to update the bitmask with characters from a string
        def update_bit(bit_mask, string):
            for c in string:
                # checking if the character is already present in the bitmask
                if 1 << (ord(c) - ord('a')) & bit_mask:
                    # if character already present, return -1 indicating invalid bitmask
                    return -1
                # otherwise, update the bitmask
                bit_mask |= 1 << (ord(c) - ord('a'))
            return bit_mask
        
        # backtracking function to find the maximum length of unique concatenated strings
        def backtrack(bit, i):
            # base case: when all strings are processed, return 0
            if i == n:
                return 0
            # initialize max_length for current position
            max_length = 0
            # iterate over remaining strings
            for j in range(i, n):
                # update bitmask with characters of current string
                new_bit = update_bit(bit, arr[j])
                # if invalid bitmask, skip this string and proceed to the next one
                if new_bit == -1:
                    continue
                # recursively find the maximum length of unique concatenated strings
                max_length = max(max_length, len(arr[j]) + backtrack(new_bit, j+1))
            # return the maximum length found
            return max_length
        
        # start backtracking from index 0 with initial bitmask 0
        return backtrack(0,0)

if __name__ == '__main__':
    s = Solution()
    print(s.maxLength(["un","iq","ue"]))
    print(s.maxLength(["cha","r","act","ers"]))
    print(s.maxLength(["abcdefghijklmnopqrstuvwxyz"]))