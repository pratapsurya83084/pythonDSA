# program using python implementation of stack

class Stack:
    def __init__(self,size):
        self.size = size;
        self.stack = [];
        # self.top = self.stack[-1];
        
    # push item
    def push(self,item):
        if len(self.stack)<self.size:
            self.stack.append(item);
            print("append :",item);
    # pop item
    def pop(self):
        if len(self.stack)!=0:
            removeElem = self.stack.pop();
            print("popped element is : ",removeElem);
    # peek element print
    def peek(self):
        if self.stack[-1]:
            print("peek element is :",self.top[-1]);
        
    # check is empty ret T or F
    def isEmpty(self):
        return len(self.stack)==0;
        
    # is full
    def isFull(self):
        return len(self.stack)==self.size;
        
    # display 
    def disply(self):
        return self.stack;

s = Stack(5);
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
s.push(60) 

s.pop()
g=s.disply()         
print(g)