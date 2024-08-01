from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # initialize an empty list to store the previous row of Pascal's Triangle
        prev_row = []
        
        # iterate through each row index up to and including rowIndex
        for i in range(rowIndex + 1):
            # create a new row with all elements initialized to 1, the length
            # of the new row is i + 1
            new_row = [1] * (i + 1)
            
            # fill in the values for the current row based on the previous row
            for j in range(1, i):
                # compute the value of the current element as the sum of the element
                # directly above and the element to the left of the element above
                new_row[j] = prev_row[j - 1] + prev_row[j]
            
            # update prev_row to be the current new_row for the next iteration
            prev_row = new_row
        
        # return the last computed row, which is the rowIndex row of Pascal's Triangle
        return prev_row

if __name__ == '__main__':
    s = Solution()
    print(s.getRow(4))
    print(s.getRow(8))
    print(s.getRow(1))