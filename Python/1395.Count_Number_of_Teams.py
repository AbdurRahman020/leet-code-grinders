from typing import List

class BIT:
    def __init__(self, size):
        # initialize a BIT with a given size, the BIT uses 1-based indexing
        self.size = size
        # BIT array initialized with zeros
        self.bit_array = [0] * (size + 1)
    
    def update(self, index, value):
        while index <= self.size:
            # update the BIT array: add 'value' to the current index
            self.bit_array[index] += value
            # move to the next index to update by adding the lowest set bit
            index += index & -index
    
    def query(self, index):
        prefix_sum = 0
        while index > 0:
            # accumulate the prefix sum from the BIT array
            prefix_sum += self.bit_array[index]
            # move to the parent index to continue accumulating the sum
            index -= index & -index
        return prefix_sum

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        if not rating:
            # if the rating list is empty, return 0 as no teams can be formed
            return 0
        
        # find the maximum rating in the list to determine the size of BIT
        max_rating = max(rating)
        
        # initialize two BITs, one for tracking the counts of ratings to 
        # the left and one for the right of the current index
        left_BIT = BIT(max_rating)
        right_BIT = BIT(max_rating)
        
        # populate the right BIT with the count of each rating; initially, all ratings 
        # are on the right side
        for r in rating:
            right_BIT.update(r, 1)
        
        team_count = 0
        
        for r in rating:
            # as we process each rating, update the right BIT to remove the current rating,
            # since it is now being considered and should not be counted in the right BIT
            right_BIT.update(r, -1)
            
            # calculate the number of ratings smaller than 'r' on the left side and on the right side
            left_smaller = left_BIT.query(r - 1)
            right_smaller = right_BIT.query(r - 1)
            
            # calculate the number of ratings larger than 'r' on the left side and on the right side
            left_larger = left_BIT.query(max_rating) - left_BIT.query(r)
            right_larger = right_BIT.query(max_rating) - right_BIT.query(r)
            
            # count the number of valid teams that can be formed with 'r' as the middle element
            # teams are counted based on two scenarios:
            #   i. ratings smaller than 'r' on the left and ratings larger than 'r' on the right
            #  ii. ratings larger than 'r' on the left and ratings smaller than 'r' on the right
            team_count += left_smaller * right_larger + left_larger * right_smaller
            
            # update the left BIT to include the current rating 'r' for subsequent calculations
            left_BIT.update(r, 1)
        
        return team_count

if __name__ == '__main__':
    s = Solution()
    print(s.numTeams([1,2,3,4]))
    print(s.numTeams([2,1,3]))
    print(s.numTeams([2,5,3,4,1]))