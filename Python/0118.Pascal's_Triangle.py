class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        pascal_triangle = []
        
        for i in range(numRows):
            rows = [0]*(i+1)
            for j in range(i+1):
                if j == 0 or j == i:
                    rows[j] = 1
                else:
                    rows[j] = pascal_triangle[i-1][j-1] + pascal_triangle[i-1][j]
            pascal_triangle.append(rows)
            
        return pascal_triangle

if __name__ == '__main__':
    s = Solution()
    print(s.generate(5))
    print(s.generate(1))
    print(s.generate(8))