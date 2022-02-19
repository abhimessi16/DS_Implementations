"""
Using a modified version of queue to find the minimum in it.
But not all values are stored, I have to read about all the other implementations
"""

def push(q,value):
    if q and value>q[-1]:
        return
    while q and q[-1]>value:
        q.pop(-1)
    q.append(value)

def remove1(q,value):
    if q and q[0]==value:
        q.pop(0)

def minimum(q):
    return q[0]

q=[]
for i in range(100,201):
    push(q,i)
    if i%5==0:
        remove1(q,i-4)
print(minimum(q))