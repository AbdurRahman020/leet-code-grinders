from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        base_satisfied = 0
        
        # calculate the initial satisfied customers without considering the 'minutes' sliding window
        for i in range(n):
            if grumpy[i] == 0:
                base_satisfied += customers[i]
        
        # calculate the maximum additional satisfied customers by applying the 'minutes' sliding window
        max_additional = base_satisfied
        
        # compute the additional satisfied customers for the first 'minutes' minutes
        for i in range(minutes):
            if grumpy[i] == 1:
                max_additional += customers[i]
        
        current_additional = max_additional
        
        # slide the 'minutes' window across the remaining customers
        for i in range(minutes, n):
            start = i - minutes
            
            # adjust the current additional satisfied customers by removing the effect of the customer 
            # 'going away' from the window
            if grumpy[start] == 1:
                current_additional -= customers[start]
            
            # add the effect of the new customer 'coming into' the window
            if grumpy[i] == 1:
                current_additional += customers[i]
            
            # update the maximum additional satisfied customers found so far
            max_additional = max(max_additional, current_additional)
        
        return max_additional

if __name__ == '__main__':
    s = Solution()
    print(s.maxSatisfied([1,0,1,2,1,1,7,5], [0,1,0,1,0,1,0,1], 3))
    print(s.maxSatisfied([1], [0], 1))