class Solution:
    def checkRecord(self, n: int) -> int:
        # define the modulo value
        mod = 10**9 + 7
        
        # initialize a 3D array for dynamic programming
        # dp[day][absences][late] represents the number of attendance records for a given day
        # day: current day
        # absences: number of absent days so far
        # late: consecutive late days so far
        dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]
        
        # initialize the starting point with 1 possibility (no absences, no lates)
        dp[0][0][0] = 1
        
        # loop through each day
        for day in range(n):
            # iterate over possible number of absences
            for absences in range(2):
                # iterate over possible number of lates
                for late in range(3):
                    # if no possibility for this combination, skip
                    if dp[day][absences][late] == 0:
                        continue
                    
                    # add 'P' (present)
                    dp[day + 1][absences][0] = (
                        dp[day + 1][absences][0] + dp[day][absences][late]
                    ) % mod
                    
                    # add 'L' (late)
                    if late < 2:
                        dp[day + 1][absences][late + 1] = (
                            dp[day + 1][absences][late + 1] + dp[day][absences][late]
                        ) % mod
                    
                    # add 'A' (absence)
                    if absences < 1:
                        dp[day + 1][absences + 1][0] = (
                            dp[day + 1][absences + 1][0] + dp[day][absences][late]
                        ) % mod
        
        # calculate the total possibilities by summing up all combinations of absences
        # and lates for the last day
        total_possibilities = 0
        for absences in range(2):
            for late in range(3):
                total_possibilities = (
                    total_possibilities + dp[n][absences][late]
                ) % mod
        
        return total_possibilities

if __name__ == "__main__":
    s = Solution()
    print(s.checkRecord(2))
    print(s.checkRecord(1))
    print(s.checkRecord(10101))