from typing import List

class Solution:
    def increasingTriplet1(self, nums: List[int]) -> bool:
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
    
    def increasingTriplet2(self, nums: List[int]) -> bool:
        # get the length of list
        n = len(nums)
        
        # using any() function to check if there exists any triplet (i, j, k) 
        # where i < j < k and nums[i] < nums[j] < nums[k]
        # if any such triplet exists, return True; otherwise, return False
        return any(
            nums[i] < nums[j] < nums[k]
            for i in range(n)               # iterate over all possible values of i
            for j in range(i + 1, n)        # iterate over all possible values of j such that j > i
            for k in range(j + 1, n)        # iterate over all possible values of k such that k > j
            )


if __name__ == '__main__':
    s = Solution()
    
    print(s.increasingTriplet1([1,2,3,4,5]))
    print(s.increasingTriplet1([5,4,3,2,1]))
    print(s.increasingTriplet1([2,1,5,0,4,6]))
    
    print(s.increasingTriplet2([1,2,3,4,5]))
    print(s.increasingTriplet2([5,4,3,2,1]))
    print(s.increasingTriplet2([2,1,5,0,4,6]))