class CircularQueue:
    def __init__(self, capacity):
        self.queue = [0] * capacity  # Array to hold the queue elements
        self.capacity = capacity
        self.front = 0  # Front pointer
        self.rear = 0   # Rear pointer
        self.count = 0  # Variable to track the number of elements in the queue

    def enqueue(self, element):
        # Check if the queue is full
        if self.isFull == True:
            print("The queue is full, try later.")
            return
        # Add the element to the queue
        self.queue[self.rear] = element
        self.rear = (self.rear + 1) % self.capacity  # Circular increment
        self.count += 1
        print(f'{element} is added successfully.')

    def dequeue(self):
        # Check if the queue is empty
        if self.count == 0:
            print('Queue is empty, try later.')
            return -1    
        # Remove the element from the front of the queue
        element = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity  # Circular increment
        self.count -= 1
        print(f'{element} is removed successfully.')
        return element

    def isFull(self):
        # Queue is full if count reaches capacity
        return self.count == self.capacity

    def isEmpty(self):
        # Queue is empty if count is 0
        return self.count == 0

    def size(self):
        # The size is simply the count of elements
        return self.count

    def display(self):
        if (self.isEmpty()==True):
            print("Queue is empty!")
            return
        idx = self.front
        while idx != self.rear:
            print(self.queue[idx], end=" ")
            idx = (idx + 1) % self.capacity

# Example usage
q = CircularQueue(5)

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)  # Queue is now full

q.display()  # Output: 10 20 30 40 50

q.dequeue()  # Removes 10
q.dequeue()  # Removes 20
q.display()  # Output: 30 40 50

q.enqueue(60)  # Adding a new element after dequeue
q.display()  # Output: 30 40 50 60