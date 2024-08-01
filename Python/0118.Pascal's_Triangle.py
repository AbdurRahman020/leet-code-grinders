from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # initialize an empty list to store the rows of Pascal's Triangle
        pascal_triangle = []
        
        # iterate through the range of numRows to construct each row of the triangle
        for i in range(numRows):
            # create a new row with all elements initialized to 0, the number
            # of elements in the current row is i+1
            rows = [0] * (i + 1)
            
            # fill in the values for the current row
            for j in range(i + 1):
                # the first and last elements of each row are always 1
                if j == 0 or j == i:
                    rows[j] = 1
                else:
                    # for all other elements, compute the value as the sum of the element
                    # directly above and the element to the left of the element above
                    rows[j] = pascal_triangle[i - 1][j - 1] + pascal_triangle[i - 1][j]
            
            # append the completed row to the Pascal's Triangle list
            pascal_triangle.append(rows)
        
        # return the fully constructed Pascal's Triangle
        return pascal_triangle

if __name__ == '__main__':
    s = Solution()
    print(s.generate(5))
    print(s.generate(1))
    print(s.generate(8))