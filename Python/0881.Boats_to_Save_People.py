from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # sort the list of people in non-decreasing order of their weights
        people.sort()
        # initialize the number of boats needed
        num_of_boats = 0
        # initialize two pointers, one at the beginning and one at the end of 
        # the sorted list
        i, j = 0, len(people) - 1
        
        # loop until the two pointers meet or cross each other
        while i <= j:
            # check if the combined weight of the heaviest and lightest person 
            # is within the limit
            if people[i] + people[j] <= limit:
                # if yes, the lightest person can be paired with the heaviest person,
                # so move the pointer for the lightest person to the next person
                i += 1
            
            # move the pointer for the heaviest person to the next person
            j -= 1
            # increment the number of boats needed, as we're sending out a boat 
            # in each iteration
            num_of_boats += 1
        
        # return the total number of boats needed
        return num_of_boats

if __name__ == '__main__':
    s = Solution()
    print(s.numRescueBoats([1,2], 3))
    print(s.numRescueBoats([3,2,2,1], 3))
    print(s.numRescueBoats([3,5,3,4], 5))