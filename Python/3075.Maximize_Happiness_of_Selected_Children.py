from typing import List

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        # sorting the happiness array in descending order
        happiness.sort(reverse=True)
        total_happiness = 0
        
        # iterating through the first 'k' elements of the sorted happiness array
        for turn in range(k):
            # if the current happiness is less than the turn number, break the loop
            if happiness[turn] < turn:
                break
            
            # calculate the total happiness by subtracting the turn number from the current happiness
            total_happiness += (happiness[turn] - turn)
        
        # return the total happiness
        return total_happiness

if __name__ == '__main__':
    s = Solution()
    print(s.maximumHappinessSum([1,2,3], 2))
    print(s.maximumHappinessSum([1,1,1,1], 2))
    print(s.maximumHappinessSum([2,3,4,5], 1))