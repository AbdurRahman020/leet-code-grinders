class Solution:
    def checkRecord(self, n: int) -> int:
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
    print(s.checkRecord(2))
    print(s.checkRecord(1))
    print(s.checkRecord(10101))