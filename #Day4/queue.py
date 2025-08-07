class myqueue:
    def __init__(self,capacity):
        self.queue = [0]*capacity
        self.capacity = capacity
        self.front = 0
        self.rear = 0

    def enqueue(self,element):
        if self.isFull()==True:
            print("the queue is full,Try later")
            return
        self.queue[self.rear]=element
        self.rear = self.rear+1
        print(f'{element }is added successfully')

    def dequeue(self):
        if self.isEmpty()==True:
            print('queue is empty, try later')
            return -1
        element=self.queue[self.front]
        self.front=self.front+1
        print(f'{element} is removed sucessfully')

    def isFull(self):
        if self.rear==self.capacity:
            return True
        else:
            return False
    
    def isEmpty(self):
        if self.front==self.rear:
            return True
        else:
            return False
        
    def size(self):
        return self.rear-self.front
    
    def display(self):
        if self.isEmpty()==True:
            print("Queue is empty!")
            return
        for i in range(self.front, self.rear + 1):
            print(self.queue[i], end=" ")
            



    
q=myqueue(6)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)

q.dequeue()
q.display()