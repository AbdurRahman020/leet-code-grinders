from typing import List
from collections import defaultdict

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        # get the length of the input array
        n = len(arr)
        # initialize a list to store the prefix XOR values
        prefix_xor = [0] * (n + 1)
        
        # calculate the prefix XOR values for the array
        for i in range(n):
            prefix_xor[i + 1] = prefix_xor[i] ^ arr[i]
        
        # initialize two dictionaries to keep track of counts and totals
        count = defaultdict(int)    # stores count of prefix XOR values
        total = defaultdict(int)    # stores total positions of prefix XOR values
        # initialize the result variable to count triplets
        result = 0
        
        # loop through the array to find triplets
        for j in range(n):
            # check if the prefix XOR value at position j+1 has occurred before
            if prefix_xor[j + 1] in count:
                # if it has occurred, update the result using count and total
                result += count[prefix_xor[j + 1]] * j - total[prefix_xor[j + 1]]
            
            # increment the count and total for the current prefix XOR value
            count[prefix_xor[j]] += 1
            total[prefix_xor[j]] += j
        
        # return the final result
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.countTriplets([2,3,1,6,7]))
    print(s.countTriplets([1,1,1,1,1]))