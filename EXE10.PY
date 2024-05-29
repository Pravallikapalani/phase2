def enqueue(q,ele):
    q.append(ele)
    print(ele,"inserted into queue sucessfully")
def dequeue(q):
    if len(q)==0:
        print("queue is empty")
        return
    print(q[0],"deleted successfully")
    q.pop(0)
q=[]
enqueue(q,10)
enqueue(q,20)
enqueue(q,30)
enqueue(q,40)
enqueue(q,50)
print(q)
dequeue(q)
dequeue(q)
dequeue(q)
dequeue(q)
dequeue(q)
dequeue(q)
print(q)
