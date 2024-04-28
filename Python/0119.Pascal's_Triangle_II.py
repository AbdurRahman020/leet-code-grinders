class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        prev_row = []
        
        for i in range(rowIndex+1):
            new_row = [1]*(i+1)
            for j in range(1,i):
                new_row[j] = prev_row[j-1] + prev_row[j]
            prev_row = new_row
            
        return new_row

if __name__ == '__main__':
    s = Solution()
    print(s.getRow(4))
    print(s.getRow(8))
    print(s.getRow(1))