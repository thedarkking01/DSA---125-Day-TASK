#User function Template for python3

class MyQueue:
    def __init__(self):
        self.queue=[]
    
    #Function to push an element x in a queue.
    def push(self, x):
        self.queue.append(x)
         
         #add code here
     
    #Function to pop an element from queue and return that element.
    def pop(self): 
        if len(self.queue) == 0:
            return -1
        else:
            return self.queue.pop(0)
         
         # add code here
