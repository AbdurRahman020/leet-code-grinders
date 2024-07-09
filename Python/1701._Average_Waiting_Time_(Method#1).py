from typing import List

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        # initialize variable to store total waiting time
        total_waiting_time = 0
        # initialize current time, start at the time of arrival of the first customer
        current_time = customers[0][0]
        
        # iterate through each customer's data [arrival_time, cooking_time]
        for arrival_time, cooking_time in customers:
            # assume chef is ready at the current time
            preparation_time = current_time
            
            # if the current customer arrives after the chef is ready, update the
            # preparation time to start serving at the customer's arrival time
            if arrival_time >= preparation_time:
                preparation_time = arrival_time
            
            # calculate when the dish will be ready
            preparation_time += cooking_time
            
            # calculate the waiting time for the current customer and add to total
            total_waiting_time += (preparation_time - arrival_time)
            # update the current time to when the current customer's dish is ready
            current_time = preparation_time
        
        # calculate and return the average waiting time across all customers
        return total_waiting_time / len(customers)

if __name__ == '__main__':
    s = Solution()
    print(s.averageWaitingTime([[1,2],[2,5],[4,3]]))
    print(s.averageWaitingTime([[5,2],[5,4],[10,3],[20,1]]))
    print(s.averageWaitingTime([[2,3],[6,3],[7,5],[11,3],[15,2],[18,1]]))