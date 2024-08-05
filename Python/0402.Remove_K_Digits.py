class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # initialize an empty list to use as a stack
        stack = []
        
        # iterate through each character in the input string `num`
        for i in range(len(num)):
            # while the stack is not empty, we still have digits to remove (k > 0),
            # and the last digit in the stack is greater than the current digit,
            # pop the last digit from the stack to make the number smaller
            while stack and k > 0 and stack[-1] > num[i]:
                stack.pop()
                k -= 1
            
            # Push the current digit onto the stack
            stack.append(num[i])
        
        # if there are still digits left to remove (k > 0), remove them from the end 
        # of the stack
        while k > 0:
            stack.pop()
            k -= 1
        
        # remove leading zeros from the stack (i.e., from the beginning of the list)
        while  len(stack) > 0 and stack[0] == '0':
            stack.pop(0)
        
        # convert the stack list to a string and return it, if the stack is empty, return '0'
        return ''.join(stack) if stack else '0'

if __name__ == '__main__':
    s = Solution()
    print(s.removeKdigits("1432219", 3))
    print(s.removeKdigits("10200", 1))
    print(s.removeKdigits("10", 2))