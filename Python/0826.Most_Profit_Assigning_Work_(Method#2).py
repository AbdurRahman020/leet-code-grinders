from typing import List

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # create a list of tuples (difficulty, profit) and sort it by difficulty
        jobs = sorted(zip(difficulty, profit))
        # sort workers' abilities
        worker.sort()
        
        # initialize total profit to be returned
        total_profit = 0
        # initialize index of the current job being considered
        target_index = 0
        # initialize maximum profit encountered so far for jobs with difficulty <= current worker's ability
        max_profit_seen_so_far = 0
        
        # iterate through each worker's ability
        for ability in worker:
            # update max_profit_seen_so_far for jobs with difficulty <= current worker's ability
            while target_index < len(jobs) and jobs[target_index][0] <= ability:
                max_profit_seen_so_far = max(max_profit_seen_so_far, jobs[target_index][1])
                target_index += 1
            # accumulate the maximum profit achievable for the current worker
            total_profit += max_profit_seen_so_far
        
        # return the total accumulated profit for all workers
        return total_profit

if __name__ == '__main__':
    s = Solution()
    print(s.maxProfitAssignment([2,4,6,8,10], [10,20,30,40,50], [4,5,6,7]))
    print(s.maxProfitAssignment([85,47,57], [24,66,99], [40,25,25]))
    print(s.maxProfitAssignment([68,35,52,47,86], [67,17,1,81,3], [92,10,85,84,82]))