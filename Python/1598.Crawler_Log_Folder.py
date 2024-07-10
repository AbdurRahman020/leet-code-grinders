from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        # initialize an empty stack to keep track of current directory levels
        stack = []
        
        # iterate through each log entry
        for log_entry in logs:
            # check if the stack is not empty and the log entry indicates moving up one directory
            if stack and log_entry == '../':
                # pop from the stack to simulate moving up one directory level
                stack.pop()
            # check if the log entry is not indicating the current directory or moving up one directory
            elif log_entry != '../' and log_entry != './':
                # if the log entry represents entering a directory, push it onto the stack
                stack.append(log_entry)
        
        # the length of the stack represents the minimum number of operations needed
        # to reach the final directory structure after processing all log entries
        return len(stack)

if __name__ == '__main__':
    s = Solution()
    print(s.minOperations(["d1/","d2/","../","d21/","./"]))
    print(s.minOperations(["d1/","d2/","./","d3/","../","d31/"]))
    print(s.minOperations(["d1/","../","../","../"]))