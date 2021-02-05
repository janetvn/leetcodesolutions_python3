class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = float('inf')

    def push(self, x):
        self.stack.append(x)
        if x < self.min_val:
            self.min_val = x

    def pop(self):
        item = self.stack.pop()
        if self.stack:
            self.min_val = min(self.stack)
        else:
            self.min_val = float('inf')
        return item

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_val

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
