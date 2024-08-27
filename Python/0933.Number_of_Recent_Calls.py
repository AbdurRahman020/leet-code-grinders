class RecentCounter:

    def __init__(self):
        # initialize an empty list to store the request timestamps
        self.requests = []
        # initialize the starting index of the window for counting requests
        self.window_start = 0

    def ping(self, t: int) -> int:
        # add the current request timestamp to the list of requests
        self.requests.append(t)
        # adjust the start of the window to ensure all requests within the last 3000 ms are counted
        while self.requests[self.window_start] < t - 3000:
            self.window_start += 1
        
        # return the number of requests within the last 3000 ms
        return len(self.requests) - self.window_start

if __name__ == '__main__':
    commands = ["RecentCounter", "ping", "ping", "ping", "ping"]
    inputs = [[], [1], [100], [3001], [3002]]
    
    obj = None
    results = []
    for i in range(len(commands)):
        command = commands[i]
        if command == "RecentCounter":
            obj = RecentCounter()
            results.append(None)
        elif command == "ping":
            t = inputs[i][0]
            result = obj.ping(t)
            results.append(result)
    
    print(results)