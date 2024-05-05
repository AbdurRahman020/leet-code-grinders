class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        # initialize variables to store maximum area and a stack to track heights and their indices
        max_area, stack = 0, [(0,0)]
        # add a sentinel to the end of the heights list to ensure all heights are processed
        heights.append(0)
        
        # iterate through each height in the heights list along with its index
        for index, height in enumerate(heights) :
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

    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        """
        Calculates the area of the largest rectangle contained within the binary matrix.

        This method finds the largest rectangle contained within the binary matrix by calculating
        the histogram of each row and then applying the largest rectangle area algorithm.

        :param matrix: A binary matrix where each cell contains '1' or '0'.
        :type matrix: list[list[str]]
        
        :return: The area of the largest rectangle contained within the binary matrix.
        :rtype: int
        """
        # initialize variables to store maximum area and height of each column
        max_area = 0
        height = [0] * len(matrix[0])
        # get the number of rows and columns in the matrix
        row_length, col_length = len(matrix), len(matrix[0])
        
        # iterate through each row of the matrix
        for i in range(row_length):
            # iterate through each column of the matrix
            for j in range(col_length):
                # if the current cell contains '1', increment the height of the corresponding column
                if matrix[i][j] == '1':
                    height[j] += 1
                # if the current cell contains '0', reset the height of the corresponding column to 0
                else:
                    height[j] = 0
            
            # calculate the maximum rectangle area for the current row and update max_area if necessary
            area = self.largestRectangleArea(height)
            max_area = max(max_area, area)
        
        # return the maximum area found
        return max_area

if __name__ == '__main__':
    s = Solution()
    print(s.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
    print(s.maximalRectangle([["0"]]))
    print(s.maximalRectangle([["1"]]))