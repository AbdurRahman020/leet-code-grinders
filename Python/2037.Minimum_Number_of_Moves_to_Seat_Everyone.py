from typing import List

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # sort the lists to make sure seats and students are in ascending order
        seats.sort()
        students.sort()
        
        # initialize a variable to store the total moves needed
        total_moves = 0
        # get the length of the seats list
        n = len(seats)
        
        # iterate through each seat-student pair
        for i in range(n):
            # calculate the absolute difference between the current seat and student
            total_moves += abs(seats[i] - students[i])
        
        # return the total moves required
        return total_moves
        
        # one line implementation
        #return sum(abs(a - b) for a, b in zip(sorted(students), sorted(seats)))

if __name__ == '__main__':
    s = Solution()
    print(s.minMovesToSeat([3,1,5], [2,7,4]))
    print(s.minMovesToSeat([4,1,5,9], [1,3,2,6]))
    print(s.minMovesToSeat([2,2,6,6], [1,3,2,6]))