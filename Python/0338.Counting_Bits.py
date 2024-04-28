class Solution:
    def countBits(self, n: int) -> list[int]:
        counter = [0]
        
        for i in range(1, n+1):
            counter.append(counter[i>>1] + i%2)
        
        return counter

if __name__ == '__main__':
    s = Solution()
    print(s.countBits(5))
    print(s.countBits(9))
    print(s.countBits(2))