class StockSpanner:

    def __init__(self):
        # create an empty stack to hold prices and their corresponding spans
        self.price_stack = []

    def next(self, price: int) -> int:
        # initialize the span to 1, as every price has at least a span of 1 (itself)
        span = 1

        # while there are elements in the stack and the current price is greater or
        # equal to than or the price at the top of the stack, pop the stack
        while self.price_stack and price >= self.price_stack[-1][0]:
            # add the span of the popped price to the current span
            span += self.price_stack.pop()[1]
        
        # push the current price and its computed span onto the stack
        self.price_stack.append([price, span])

        # return the computed span for the current price
        return span

if __name__ == '__main__':
    commands = ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
    inputs = [[], [100], [90], [95], [80], [85], [110], [105]]
    
    obj = None
    results = []
    
    for i in range(len(commands)):
        command = commands[i]
        if command == "StockSpanner":
            obj = StockSpanner()
            results.append(None)
        elif command == "next":
            price = inputs[i][0]
            result = obj.next(price)
            results.append(result)
    
    print(results)