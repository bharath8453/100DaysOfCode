class Mystack:
    def __init__(self,capacity):
        self.stack=[0]*capacity
        self.top=-1
        self.capacity=capacity

    def push(self,element):
        if(self.top==self.capacity-1):
            print("stack overflow")
            return
        self.top+=1
        self.stack[self.top]=element

    def pop(self):
        if (self.isEmpty()==True):
            print("stackunderflow")
            return -1
        element=self.stack[self.top]
        self.top-=1
        return element
    
    def peek(self):
        if self.isEmpty():
            print("stack is empty")
            return None
        return self.stack[self.top]
    
    def display(self):
        if self.isEmpty():
            print("stack is empty")
            return
        print("stack elements(top to bottom):")
        for i in range(self.top,-1,-1):
            print(self.stack[i])
            
    def isEmpty(self):
        return self.top==-1
    
    def size(self):
        print("Current stack size:", self.top + 1)
        return self.top + 1
    
s1=Mystack(5)
s1.push(100)
s1.push(200)
s1.push(300)


s1.display()
print("top element is:",s1.peek())
s1.pop()
print("after popping one element:")
s1.display()
s1.size()

element=s1.pop()
print(element)