class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for i in range(len(num)):
            while stack and k > 0 and stack[-1] > num[i]:
                stack.pop()
                k -= 1 
            stack.append(num[i])
        
        while k > 0:
            stack.pop()
            k -= 1

        while  len(stack) > 0 and stack[0] == '0':
            stack.pop(0)
        
        return ''.join(stack) if stack else '0'

if __name__ == '__main__':
    s = Solution()
    print(s.removeKdigits("1432219", 3))
    print(s.removeKdigits("10200", 1))
    print(s.removeKdigits("10", 2))