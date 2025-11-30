# class StaticQueue:
#     def __init__(self, size):
#         self.size = size
#         self.queue = [None] * size
#         self.front = -1
#         self.rear = -1

#     def isFull(self):
#         return self.rear == self.size - 1

#     def isEmpty(self):
#         return self.front == -1 or self.front > self.rear

#     def enqueue(self, item):
#         if self.isFull():
#             print("Queue is Full")
#             return

#         if self.front == -1:
#             self.front = 0   #  redeclared by 0 

#         self.rear += 1   # -1+1=0th index 
#         self.queue[self.rear] = item
#         print("Enqueued:", item)

#     def dequeue(self):
#         if self.isEmpty():
#             print("Queue is Empty")
#             return

#         removed = self.queue[self.front]
#         print("Dequeued:", removed)
#         self.front += 1

#     def displayqueue(self):
#         if self.isEmpty():
#             print("Queue is Empty")
#         else:
#             print("Queue contents:", self.queue[self.front:self.rear + 1])


# q = StaticQueue(5)
# q.enqueue(10)
# q.enqueue(20)
# q.enqueue(30)
# q.enqueue(40)
# q.enqueue(50)
# q.displayqueue()

# q.dequeue()
# q.displayqueue()

# print("Is Full:", q.isFull())
# print("Is Empty:", q.isEmpty())








#  isfull , isEmpty , enqueue , dequeue , display

class QueueStatic:
    def __init__(self,size):
        self.size  = size
        self.queue = [None]*size  # [None,None,None,None]
        self.front = -1
        self.rear = -1

    # function for check queue isEmpty isFull
    def isEmpty(self):
        return self.front == -1
    #fun for isFULL
    def isFull(self):
        return self.rear == self.size-1

    #enqueue or insert function
    def enqueue(self , item):
        if self.isFull():
            print("queue is already Full , you can't insert items")
            return
        else:
            if self.front==-1:
                self.front=0
        self.rear+=1 
        self.queue[self.rear] = item
        print("Your item is insert in queue : ",item)
        return
    
    #fun for deque or delete ,pop
    def dequeue(self):
        if self.isEmpty():
            print("queue is empty , you can't delete from queue : ")
            return
        else:
            remove = self.queue[self.front]
            print("deleted item from queue is : ",remove)
            self.front+=1
            return
    # fun for display context of queue
    def displayQueue(self):
        if not self.isEmpty():
            return self.queue[self.front:self.rear-1]


q = QueueStatic(5)
q.enqueue(17)           
q.enqueue(18)           
q.enqueue(19)           
q.enqueue(20) 
q.enqueue(21) 
q.enqueue(22) 
print("before delete item from queue : ", q.displayQueue())
q.dequeue()          
print("after delete item from queue : ",q.displayQueue())

q.isEmpty()
q.isFull()


    






