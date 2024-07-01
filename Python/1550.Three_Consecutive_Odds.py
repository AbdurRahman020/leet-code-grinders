from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        # determine the length of the input list
        n = len(arr)
        # initialize a variable to keep track of the number of odd numbers in 
        # the current window
        window = 0
        
        # initialize the window with the count of odd numbers in the first 3 
        # elements or all elements if less than 3
        for i in range(min(3, n)):
            window += arr[i] % 2
        
        # check if the initial window of size up to 3 already contains 3 odd numbers
        if window == 3:
            return True
        
        # slide the window across the array from the 4th element to the end
        for i in range(3, n):
            # add the next element to the window
            window += arr[i] % 2
            # remove the element that is no longer in the window
            window -= arr[i-3] % 2
            
            # check if the current window of size 3 contains exactly 3 odd numbers
            if window == 3:
                return True
        
        # if no window of size 3 with exactly 3 odd numbers was found, return False
        return False
        
        # method#2
        # return "111" in "".join([str(i%2) for i in arr])

if __name__ == '__main__':
    s = Solution()
    print(s.threeConsecutiveOdds([2,6,4,1]))
    print(s.threeConsecutiveOdds([1,2,34,3,4,5,7,23,12]))