from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        total_time = 0
        
        for i, j in enumerate(tickets): 
            if i <= k:
                total_time += min(tickets[i], tickets[k])
            else:
                total_time += min(tickets[i], tickets[k]-1)
                
        return total_time 

if __name__ == '__main__':
    s = Solution()
    print(s.timeRequiredToBuy([2,3,2], 2))
    print(s.timeRequiredToBuy([5,1,1,1], 0))