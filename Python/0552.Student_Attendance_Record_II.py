class Solution:
    def checkRecord1(self, n: int) -> int:
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
    
    def checkRecord2(self, n: int) -> int:
        mod = 10**9 + 7
        
        # base case: if no records, there are no valid sequences
        if n == 0:
            return 0
        
        # base case: if only one record, there are three possibilities: P, A, L
        if n == 1:
            return 3
        
        # initialize an array to store the number of valid records for each length
        # the initial values represent the number of valid records for lengths 0, 1, and 2 respectively:
        # 0: represents an empty record, so there's only one possibility (no violation)
        # 1: represents a record with only 'P', also no violation
        # 2: represents a record with 'PL' or 'LP', also no violation
        # 4: represents a record with 'PPL', 'PLP', 'LPP', or 'LLL', but no more than one 'A'
        dp = [1, 2, 4] + [0] * (n - 2)
        
        # calculate sequences without 'A' using dynamic programming
        for i in range(3, n + 1):
            # the number of valid records of length 'i' is the sum of the possibilities of
            # length 'i-1', 'i-2', and 'i-3'
            dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % mod
        
        # total possibilities without 'A'
        total_possibilities = dp[n]
        
        # add sequences with 'A'
        for i in range(n):
            # multiply the number of possibilities before position 'i' with the number of
            # possibilities after position 'i'
            total_possibilities += (dp[i] * dp[n - i - 1]) % mod
        
        # return the total number of possibilities modulo mod
        return total_possibilities % mod

if __name__ == "__main__":
    s = Solution()
    
    print(s.checkRecord1(2))
    print(s.checkRecord1(1))
    print(s.checkRecord1(10101))
    
    print(s.checkRecord2(2))
    print(s.checkRecord2(1))
    print(s.checkRecord2(10101))
