from typing import List
from collections import Counter

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # count occurrences of each number in arr1
        num_count = Counter(arr1)
        # initialize an empty list to store the relative sorted array elements
        sorted_arr1 = []
        
        # iterate through arr2
        for num in arr2:
            # add num to sorted_arr1 the number of times it appears in arr1
            sorted_arr1 += [num] * num_count[num]
            # remove the counted occurrences of num from num_count
            del num_count[num]
        
        # iterate through remaining keys in num_count, sorted in ascending order
        for key in sorted(num_count.keys()):
            # add each remaining number to sorted_arr1 the number of times it appears in arr1
            sorted_arr1 += [key] * num_count[key]
        
        # return the relative sorted array
        return sorted_arr1

if __name__ == '__main__':
    s = Solution()
    print(s.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))
    print(s.relativeSortArray([28,6,22,8,44,17], [22,28,8,6]))