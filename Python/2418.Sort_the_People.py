from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # get the number of elements in the input lists
        n = len(names)
        
        # initialize an empty list to store pairs of height and name
        people_list = []
        # iterate through each index i from 0 to n-1
        for i in range(n):
            # append a pair [heights[i], names[i]] to people_list
            people_list.append([heights[i], names[i]])
        
        # sort people_list in descending order based on the first element of each pair (height)
        people_list.sort(reverse = True)
        
        # initialize an empty list to store sorted names
        sorted_names = []
        # iterate through each pair (height, name) in people_list
        for height, name in people_list:
            # append the name (second element of the pair) to sorted_names
            sorted_names.append(name)
        
        # return the sorted list of names
        return sorted_names

if __name__ == '__main__':
    s = Solution()
    print(s.sortPeople(["Mary","John","Emma"], [180,165,170]))
    print(s.sortPeople(["Alice","Bob","Bob"], [155,185,150]))