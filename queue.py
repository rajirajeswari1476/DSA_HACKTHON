class MyQueue:
    def __init__(self,capacity):
        self.queue=[0]*capacity
        self.rare=-1
        self.front=-1
        self.capacity=capacity
    def enqueue(self,element):
        if(self.isFull==True):
            print("Queue is overflow")
            return
        self.rare=self.rare+1
        self.queue[self.rare]=element
    def dequeue(self):
        if(self.isEmpty==True):
            print("queue is underflow")
            return -1
        self.front=self.front+1
        element=self.queue[self.front]
        return element
    def isFull(self):
        return self.rare==self.capacity
    def isEmpty(self):
        return self.rare==self.front
    def peek(self):
        if(self.isEmpty==True):
            print("queue is empty")
            return
        return self.queue[self.front]
    def display(self):
        if (self.isEmpty==True):
            print("queue is empty")
            return
        for i in range(self.front+1,self.rare+1):
            print(self.queue[i])
q=MyQueue(10)
q.enqueue(40)
q.enqueue(10)
q.enqueue(15)
q.enqueue(20)
q.enqueue(25)
q.enqueue(30)
b=q.dequeue()
print(f"delete element {b}")
a=q.peek()
print(f"print front element {a}")
q.isFull()
q.isEmpty()
q.display()