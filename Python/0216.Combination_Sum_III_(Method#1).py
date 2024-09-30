from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # initialize a list to store valid combinations
        combo = []

        def backtrack(curr_num, curr_combo, target_sum):
            # if the current combination has the required number of elements (k)
            if len(curr_combo) == k:
                # check if the sum of the current combination equals the target sum
                if target_sum == 0:
                    # if it does, add the combination to the results
                    combo.append(curr_combo)
                return
            
            # iterate through numbers 1 to 9 (inclusive)
            for num in range(curr_num + 1, 10):
                # proceed only if the number is less than or equal to the remaining target sum
                if num <= target_sum:
                    # recursively call backtrack with the new number included in the combination
                    backtrack(num, curr_combo + [num], target_sum - num)
                else:
                    # if the number exceeds the target sum, exit the loop early
                    return

        # start backtracking with initial values
        backtrack(0, [], n)

        # return all valid combinations found
        return combo

if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum3(3, 7))
    print(s.combinationSum3(3, 9))
    print(s.combinationSum3(4, 1))