class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack2.append(x)
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def pop(self) -> int:
        return self.stack1.pop()

    def peek(self) -> int:
        return self.stack1[-1]

    def empty(self) -> bool:
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