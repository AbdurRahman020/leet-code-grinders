from typing import Any

class MyQueue:

    def __init__(self):
        # initialize two stacks for queue implementation
        self.stack1 = []    # stack for pushing elements
        self.stack2 = []    # stack for popping elements

    def push(self, x: Any) -> None:
        # move all elements from stack1 to stack2
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        # add the new element to the bottom of stack2
        self.stack2.append(x)
        # move all elements back to stack1 to maintain queue order
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def pop(self) -> Any:
        # pop the element from the top of stack1 (front of queue)
        return self.stack1.pop()

    def peek(self) -> Any:
        # return the top element of stack1 without removing it
        return self.stack1[-1]

    def empty(self) -> bool:
        # check if stack1 is empty to determine if the queue is empty
        return not self.stack1

if __name__ == '__main__':
    myQueue = MyQueue()
    myQueue.push(1)
    myQueue.push(2)
    myQueue.push(3)
    print('peek:', myQueue.peek())
    print('pop:', myQueue.pop())
    print('pop:', myQueue.pop())
    print('peek:', myQueue.peek())
    print('empty:', myQueue.empty())