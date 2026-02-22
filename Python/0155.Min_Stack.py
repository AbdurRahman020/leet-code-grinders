class MinStack:

    def __init__(self):
        # initialize main stack
        self.stack = []
        # initialize minimum value stack
        self.minStack = []

    def push(self, val: int) -> None:
        # push value onto main stack
        self.stack.append(val)
        # if the minimum stack is empty or the value is smaller or equal
        # to the current minimum
        if not self.minStack or self.minStack[-1] >= val:
            # push value onto minimum stack
            self.minStack.append(val)

    def pop(self) -> None:
        # check if the main stack is not empty
        if self.stack:
            # if the element to pop is the current minimum
            if self.stack[-1] == self.minStack[-1]:
                # pop from minimum stack
                self.minStack.pop()
            # always pop from main stack
            self.stack.pop()

    def top(self) -> int:
        # check if the main stack is not empty
        if self.stack:
            # return the top element
            return self.stack[-1]

    def getMin(self) -> int:
        # check if the main stack is not empty
        if self.minStack:
            # return the current minimum value
            return self.minStack[-1]


if __name__ == '__main__':
    ops = ["MinStack", "push", "push", "push",
           "getMin", "pop", "top", "getMin"]
    vals = [[], [-2], [0], [-3], [], [], [], []]

    obj, output = None, []
    for op, val in zip(ops, vals):
        if op == "MinStack":
            obj = MinStack()
            output.append(None)
        elif op == "push":
            obj.push(val[0])
            output.append(None)
        elif op == "pop":
            obj.pop()
            output.append(None)
        elif op == "top":
            output.append(obj.top())
        elif op == "getMin":
            output.append(obj.getMin())

    print(output)
