from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # calculate the number of elements in the list
        n = len(heights)
        # initialize a variable to store the count of students whose heights are out of order
        count = 0
        
        # sort the list of heights to get the expected order
        expected_heights = sorted(heights)
        
        # iterate through each student's height
        for i in range(n):
            # compare the current student's height with the expected height at the same index
            if heights[i] != expected_heights[i]:
                # if the heights don't match, increment the count
                count += 1
        
        # return the count of students with heights out of order
        return count
    
    # one line implemention
    # return sum(h != e_h for h, e_h in zip(heights, sorted(heights)))

if __name__ == '__main__':
    s = Solution()
    print(s.heightChecker([1,1,4,2,1,3]))
    print(s.heightChecker([5,1,2,3,4]))
    print(s.heightChecker([1,2,3,4,5]))