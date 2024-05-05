class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        """
        Calculates the area of the largest rectangle that can be formed from the given heights.

        This method implements the algorithm to find the largest rectangle area in a histogram. 
        It utilizes a stack to efficiently find the maximum area by keeping track of the heights 
        and their indices.

        :param heights: A list of integers representing the heights of bars in a histogram.
        :type heights: list[int]
        
        :return: The area of the largest rectangle that can be formed.
        :rtype: int
        """
        # initialize variables to store maximum area and a stack to track heights and their indices
        max_area, stack = 0, [(0,0)]
        # add a sentinel to the end of the heights list to ensure all heights are processed
        heights.append(0)
        
        # iterate through each height in the heights list along with its index
        for index, height in enumerate(heights):
            # initialize the starting index for calculating the width of the rectangle
            start = index
            # while the current height is less than the height at the top of the stack
            while stack[-1][0] > height:
                # pop the top height and index from the stack
                h, i = stack.pop()
                # calculate the area of the rectangle with the popped height and index
                max_area = max(max_area, (index-i)*h)
                # update the starting index for calculating the width of the rectangle
                start = i 
            
            # if the current height is greater than the height at the top of the stack
            if height > stack[-1][0]:
                # append the current height and its corresponding starting index to the stack
                stack.append((height, start))
        
        # return the maximum area found
        return max_area

if __name__ == '__main__':
    s = Solution()
    print(s.largestRectangleArea([2,4]))
    print(s.largestRectangleArea([2,1,5,6,2,3]))