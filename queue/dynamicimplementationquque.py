class Queue:
    def __init__(self):
        self.queue = []  # array (list)

    # Enqueue → insert element at end
    def enqueue(self, item):
        self.queue.append(item)
        print(f"Inserted: {item}")

    # Dequeue → remove element from front
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty! Cannot dequeue.")
            return None
        return self.queue.pop(0)

    # Peek → return front element
    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]

    # Check if queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Size of queue
    def size(self):
        return len(self.queue)



q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Dequeued:", q.dequeue())
print("Front element:", q.peek())
print("Queue size:", q.size())
