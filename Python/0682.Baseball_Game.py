class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack = []
        
        for i in range(len(operations)):
            if operations[i] != 'C' and operations[i] != 'D' and operations[i] != '+':
                stack.append(int(operations[i]))
            elif operations[i] == 'C':
                stack.pop()
            elif operations[i] == 'D':
                stack.append(stack[-1]*2)
            elif operations[i] == '+':
                stack.append(stack[-1] + stack[-2])
                
        return sum(stack)

if __name__ == '__main__':
    s = Solution()
    print(s.calPoints(["5","2","C","D","+"]))
    print(s.calPoints(["5","-2","4","C","D","9","+","+"]))
    print(s.calPoints(["1","C"]))