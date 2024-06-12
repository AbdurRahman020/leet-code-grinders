from typing import List

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        # get the dimensions of the matrix
        row_length, col_length = len(matrix), len(matrix[0])

        # precompute cumulative sums for each row
        for r in range(row_length):
            for c in range(1, col_length):
                matrix[r][c] += matrix[r][c - 1]

        # initialize the variable to store the count of submatrices with the target sum
        result = 0

        # iterate over all possible start and end columns for submatrices
        for start_col in range(col_length):
            for end_col in range(start_col, col_length):
                # initialize a dictionary to store prefix sums and their counts
                sum_count = {0: 1}
                # initialize the prefix sum for the current submatrix
                prefix_sum = 0

                # iterate over each row of the matrix
                for r in range(row_length):
                    # calculate the sum of the current submatrix
                    prefix_sum += matrix[r][end_col] - (matrix[r][start_col - 1] if start_col > 0 else 0)
                    # update the total count with the count of submatrices with the target sum
                    result += sum_count.get(prefix_sum - target, 0)
                    # update the count of prefix sums encountered
                    sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1
        
        # return the final count of matrices
        return result

if __name__ == '__main__':
    # Test cases
    s = Solution()
    print(s.numSubmatrixSumTarget([[0,1,0],[1,1,1],[0,1,0]], 0))
    print(s.numSubmatrixSumTarget([[904]], 0))
    print(s.numSubmatrixSumTarget([[1,-1],[-1,1]], 0))
