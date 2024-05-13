class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        # find the maximum number of candies among all kids
        _max = max(candies)
        # initialize an empty list to store the result
        result = []
        
        for x in candies:
            # check if the current kid can have the maximum number of candies 
            # by adding extraCandies
            if x + extraCandies >= _max:
                # if yes, append True to the result list    
                result.append(True)
            else:
                # if no, append False to the result list
                result.append(False)
        
        # return the list of booleans indicating whether each kid can have 
        # the maximum number of candies
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.kidsWithCandies([2,3,5,1,3], 3))
    print(s.kidsWithCandies([4,2,1,1,2], 1))
    print(s.kidsWithCandies([12,1,12], 10))