

class DynamicStack:
    def __init__(self):
        self.stack = []
 # push stack function
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) == 0:
            return"stack is empty , you cannot pop"
        else:
            return  self.stack.pop()
    def peek(self):
        if len(self.stack)!=0:
            return self.stack[-1]
        else:
            return "stack is empty , you cannot peek"

    def display(self):
        return self.stack        




s1 = DynamicStack()

s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)

print("after adding element : ", s1.display())
print("after popping element : ", s1.pop())
print("peek element : ", s1.peek())
print("final stack : ", s1.display())





