from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # initialize two variables to hold the smallest and second smallest values
        smallest, middle = float('inf'), float('inf')
        
        # iterate through each number in the list
        for num in nums:
            # if the current number is smaller than or equal to the smallest,
            # update the smallest value
            if num <= smallest:
                smallest = num
            # if the current number is smaller than or equal to the middle,
            # but greater than the smallest, update the middle value
            elif num <= middle:
                middle = num
            # if the current number is greater than the middle,
            # we found a triplet, so return True
            elif num > middle:
                return True
        
        # if no triplet is found, return False
        return False 

if __name__ == '__main__':
    s = Solution()
    print(s.increasingTriplet([1,2,3,4,5]))
    print(s.increasingTriplet([5,4,3,2,1]))
    print(s.increasingTriplet([2,1,5,0,4,6]))