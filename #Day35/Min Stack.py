class MinStack(object):
    def __init__(self):
        # main stack to store values
        self.stack = []
        # min stack to store current minimums
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        # if min_stack empty OR new val <= current min, push it to min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.stack:
            val = self.stack.pop()
            # if popped value is the current min, remove it from min_stack too
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self):
        return self.stack[-1] if self.stack else None

    def getMin(self):
        return self.min_stack[-1] if self.min_stack else None

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin()) 
minStack.pop()
print(minStack.top())   
print(minStack.getMin())