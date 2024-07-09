from typing import List

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        # initialize variable to store total waiting time
        total_waiting_time = 0
        # initialize current time, start at the time of arrival of the first customer
        current_time = customers[0][0]
        
        # iterate through each customer's data [arrival_time, cooking_time]
        for arrival_time, cooking_time in customers:
            
            if current_time >= arrival_time:
                # case 1: If the chef is ready by the customer's arrival time
                total_waiting_time += current_time - arrival_time + cooking_time
            else:
                # case 2: If the chef is not ready by the customer's arrival time
                total_waiting_time += cooking_time
            
            # determine when the chef finishes with the current customer
            current_time = max(current_time + cooking_time, arrival_time + cooking_time)
        
        # calculate and return the average waiting time across all customers
        return total_waiting_time / len(customers)

if __name__ == '__main__':
    s = Solution()
    print(s.averageWaitingTime([[1,2],[2,5],[4,3]]))
    print(s.averageWaitingTime([[5,2],[5,4],[10,3],[20,1]]))
    print(s.averageWaitingTime([[2,3],[6,3],[7,5],[11,3],[15,2],[18,1]]))