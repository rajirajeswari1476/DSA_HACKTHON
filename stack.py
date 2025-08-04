class MyStack:
    def __init__(self,capacity):
        self.stack=[0]*capacity
        self.top=-1
        self.capacity=capacity
    def push(self,element):
        if(self.isFull==True):
            print("stach is overflow")
            return
        self.top=self.top+1
        self.stack[self.top]=element
    def pop(self):
        if(self.isEmpty==True):
            print("Stack is underflow")
            return -1
        element=self.stack[self.top]
        self.top=self.top-1
        return element
    def isFull(self):
        return self.top==self.capacity-1
    def isEmpty(self):
        return self.top==-1
    def peek(self):
        if(self.isEmpty==True):
            print("stack is empty")
            return
        return self.stack[self.top]
    def display(self):
        if(self.isEmpty==True):
            print("stack is empty")
        for i in range(self.top+1):
            print(self.stack[i])
s=MyStack(10)
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
a=s.pop()
print(f"delement {a}")
b=s.peek()
print(f"peek element is {b}")
s.isEmpty()
s.isFull()
s.display()















