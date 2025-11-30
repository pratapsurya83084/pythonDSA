

class StaticQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size   # fixed size array
        self.front = -1
        self.rear = -1

    # Insert element
    def enqueue(self, value):
        if self.rear == self.size - 1:
            print("Queue Overflow! Cannot insert.")
            return
        
        if self.front == -1:     # first element
            self.front = 0
        
        self.rear += 1
        self.queue[self.rear] = value
        print(f"Inserted {value}")

    # Delete element
    def dequeue(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue Underflow! Cannot delete.")
            return None
        
        removed = self.queue[self.front]
        self.front += 1
        print(f"Deleted {removed}")
        return removed

    # Display queue
    def display(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue is empty")
        else:
            print("Queue elements:", end=" ")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()

q = StaticQueue(5)

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()

q.dequeue()
q.display()

q.enqueue(40)
q.enqueue(50)
q.enqueue(60)
q.display()








