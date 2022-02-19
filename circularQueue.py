"""
implemented circular queue using lists
all operations are O(1)

satisfactory implementation
"""

class Queue:
    def __init__(self,maxsize):
        self.items=[None]*maxsize
        self.maxsize=maxsize
        self.start=-1
        self.top=-1
    
    def __str__(self):
        values=[str(x) for x in self.items]
        return " ".join(values)

    def isFull(self):
        if self.top<self.start:
            if self.top+1==self.start:
                return True
        else:
            if self.start==0 and self.top+1==self.maxsize:
                return True
        return False
    
    def isEmpty(self):
        if self.top==-1 and self.start==-1:
            return True
        return False
    
    def enqueue(self,value):
        if self.isFull():
            return
        if self.start==-1:
            self.start=0
        self.top=(self.top+1)%self.maxsize
        self.items[self.top]=value
    
    def dequeue(self):
        if self.isEmpty():
            return
        if self.start==self.top:
            d=self.items[self.start]
            self.__init__(self.maxsize)
            return d
        d=self.items[self.start]
        self.items[self.start]=None
        self.start=(self.start+1)%self.maxsize
        return d
    
    def peek(self):
        return self.items[self.start]
    
    def delete(self):
        self.__init__(self.maxsize)
    
    def size(self):
        if self.start>self.top:
            return self.maxsize-self.start+self.top+1
        return self.top-self.start+1
