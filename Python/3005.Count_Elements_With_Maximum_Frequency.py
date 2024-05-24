from typing import List
from collections import Counter

class Solution(object):
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # count the occurrences of each number in the list
        x = Counter(nums)
        # initialize the maximum frequency to -1
        max_frq = -1
        
        # loop through the Counter object
        for i in x:
            # update the maximum frequency
            max_frq = max(max_frq, x[i])
        
        # initialize a variable to store the sum of elements with maximum frequency
        sum = 0
        # loop through the Counter object again
        for i in x:
            # if the frequency of the current element is equal to the maximum frequency
            if x[i] == max_frq:
                # add the frequency of that element to the sum
                sum += x[i]
        
        # return the sum of elements with maximum frequency
        return sum
    
if __name__ == '__main__':
    s = Solution()
    print(s.maxFrequencyElements([1,2,2,3,1,4]))
    print(s.maxFrequencyElements([1,2,3,4,5]))