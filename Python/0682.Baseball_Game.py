from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # initialize an empty stack to keep track of the scores
        stack = []
        
        # iterate through each operation in the operations list
        for i in range(len(operations)):
            # check if the current operation is a number (not 'C', 'D', or '+')
            if operations[i] != 'C' and operations[i] != 'D' and operations[i] != '+':
                # convert the number from string to integer and push it onto the stack
                stack.append(int(operations[i]))
            # if the current operation is 'C', remove the last score from the stack
            elif operations[i] == 'C':
                stack.pop()
            # if the current operation is 'D', double the last score and push it onto the stack
            elif operations[i] == 'D':
                stack.append(stack[-1]*2)
            # if the current operation is '+', sum the last two scores and push the result onto the stack
            elif operations[i] == '+':
                stack.append(stack[-1] + stack[-2])
        
        # return the sum of all the scores in the stack
        return sum(stack)

if __name__ == '__main__':
    s = Solution()
    print(s.calPoints(["5","2","C","D","+"]))
    print(s.calPoints(["5","-2","4","C","D","9","+","+"]))
    print(s.calPoints(["1","C"]))