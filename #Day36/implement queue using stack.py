class MyQueue(object):
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x):
        self.stack_in.append(x)

    def pop(self):
        if not self.stack_out:  # move elements only if stack_out is empty
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()

    def peek(self):
        if not self.stack_out:  # move elements only if stack_out is empty
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]

    def empty(self):
        return not self.stack_in and not self.stack_out

myQueue = MyQueue()
myQueue.push(1)    
myQueue.push(2)     
print(myQueue.peek()) 
print(myQueue.pop()) 
print(myQueue.empty()) 