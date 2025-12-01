
import heapq

q=[]
# heapq.heappush(q,(100,"pratap",300))
# heapq.heappush(q,(2,"abhi",700))
# print("priority queue is :",q)

# this is question is based on name priority 

class Queue:
    def __init__(self):
        self.pqueue = []
        
    def add_patient(self,pname,pseverity):
        heapq.heappush(self.pqueue,(pname,pseverity))
        print(pname,"add patient")
    def treat_Patients(self):
        pname , pseverity = heapq.heappop(self.pqueue)   # extract pname and pseverity from queue 
        print("treated patient is :" , pname , pseverity)
    def displayPatients(self):
        print("patients are : ",self.pqueue)

pq = Queue()
pq.add_patient("john",1)                    
pq.add_patient("amit",3)                    
pq.add_patient("rohan",2)             
pq.treat_Patients()
pq.displayPatients()       





# # python how it works
# # heapq always compares the first element of the tuple.

# # So Python sorts based on names, not severity:

# # Alphabetically:

# # amit < john < rohan