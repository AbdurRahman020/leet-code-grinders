class Solution:
    def totalMoney(self, n: int) -> int:
        day, weeks, total_balance = 1, 0, 0
        
        for days in range(1, n+1):
            total_balance += (weeks + day)
            day += 1
            
            if days%7 == 0:
                weeks += 1
                day = 1
                
        return total_balance

if __name__ == '__main__':
    s = Solution()
    print(s.totalMoney(4))
    print(s.totalMoney(10))
    print(s.totalMoney(20))