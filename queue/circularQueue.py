class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, val):
        if self.is_full():
            raise IndexError("queue is overflow , can't insert element")

        if self.is_empty():
            #if true then add 0th index first item
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = val
        else:
            #rear and front are not -1 ,so false then stil inc by 1 and
            # next index new element assign
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = val

        print(f"{val} is inserted into queue")

    def dequeue(self):
        if self.is_empty():
            raise IndexError("queue is underflow , can't pop val")

        removed = self.queue[self.front]
        print(f"{removed} is pop or remove from queue")

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

    def display(self):
        if self.is_empty():
            return []

        result = []
        i = self.front
        while True:
            result.append(self.queue[i])
            if i == self.rear:
                break
            i = (i + 1) % self.size
        return result



q = CircularQueue(5)
q.enqueue(101)               
q.enqueue(102)               
q.enqueue(103)               
q.enqueue(104)               
q.enqueue(105)

q.dequeue()

result = q.display()
print("all context of Circular queue is : ",result)



