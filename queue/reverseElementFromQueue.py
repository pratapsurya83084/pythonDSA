
class RevQueueElement:
    def __init__(self):
        self.queue = []
    def enqueue(self,item):
        self.queue.append(item)
        print("append in queue :",self.queue)

    def revQueue(self):
        if self.queue:
            rev = self.queue[::-1]
            print("reversed queue is : ",rev)
        

rev = RevQueueElement()

rev.enqueue(10)  
rev.enqueue(20)
rev.enqueue(30)


rev.revQueue()
# rev.revQueue()
# rev.revQueue()

