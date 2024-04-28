class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result, total, i, j = [], 0, len(a)-1, len(b)-1
        
        while i >= 0 or j >= 0 or total:
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            result.append(str(total % 2))
            total //= 2
            
        return ''.join(reversed(result))
    
        #method 2
        #return bin(int(a,2) + int(b,2))[2:]

if __name__ == '__main__':
    s = Solution()
    print(s.addBinary("11", "1"))
    print(s.addBinary("1010", "1011"))