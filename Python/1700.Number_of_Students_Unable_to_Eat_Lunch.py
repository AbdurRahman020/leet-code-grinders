from typing import List
from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_Queue = deque(students)
        sandwich_Stack = []
        
        for sandwich in reversed(sandwiches):
            sandwich_Stack.append(sandwich)
        
        served = 0
        
        while student_Queue and served < len(student_Queue):
            if sandwich_Stack[-1] == student_Queue[0]:
                sandwich_Stack.pop()
                student_Queue.popleft()
                served = 0
            else:
                student_Queue.append(student_Queue[0])
                student_Queue.popleft()
                served += 1
        
        return len(student_Queue)

if __name__ == '__main__':
    s = Solution()
    print(s.countStudents([1,1,0,0], [0,1,0,1]))
    print(s.countStudents([1,1,1,0,0,1], [1,0,0,0,1,1]))