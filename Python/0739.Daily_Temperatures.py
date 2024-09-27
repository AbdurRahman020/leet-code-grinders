from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # get the number of temperature readings
        n = len(temperatures)
        # initialize a stack to keep track of indices of temperatures
        temp_stack = []
        # initialize the result list with zeros, to store days until warmer temperatures
        days_until_warmer = [0] * n
        
        # iterate through each temperature reading
        for i in range(n):
            # current temperature at index i
            curr_temp = temperatures[i]
            
            # while there are indices in the stack and the current temperature is higher
            # than the temperature at the index on the top of the stack
            while temp_stack and temperatures[temp_stack[-1]] < curr_temp:
                # calculate the number of days until a warmer temperature
                days_until_warmer[temp_stack[-1]] = i - temp_stack[-1]
                # remove the index from the stack since we've found a warmer temperature
                temp_stack.pop()
            
            # add the current index to the stack for future comparisons
            temp_stack.append(i)
        
        # return the list of days until warmer temperatures
        return days_until_warmer

if __name__ == '__main__':
    s = Solution()
    print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))
    print(s.dailyTemperatures([30,40,50,60]))
    print(s.dailyTemperatures([30,60,90]))