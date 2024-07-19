from typing import List

class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        # determine the dimensions of the matrix
        row_length, col_length = len(matrix), len(matrix[0])
        # list to store lucky numbers found
        lucky_num = []
        
        # iterate through each row in the matrix
        for r in range(row_length):
            # initialize minimum value to a very large number
            min_value = float('inf')
            # variable to store the column index of the minimum value
            col_index = -1
            
            # find the minimum value in the current row and its column index
            for c in range(col_length):
                if matrix[r][c] < min_value:
                    min_value = matrix[r][c]
                    col_index = c
            
            # check if the minimum value is the maximum in its column
            is_lucky = True
            for rr in range(row_length):
                if matrix[rr][col_index] > min_value:
                    is_lucky = False
                    break
            
            # if the current minimum value is a lucky number, add it to the list
            if is_lucky:
                lucky_num.append(min_value)
        
        # return the list of lucky numbers found
        return lucky_num

if __name__ == '__main__':
    s = Solution()
    print(s.luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]))
    print(s.luckyNumbers([[1,10,4,2],[9,3,8,7],[15,16,17,12]]))
    print(s.luckyNumbers([[7,8],[1,2]]))