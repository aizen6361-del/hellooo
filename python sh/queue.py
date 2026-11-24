queue=[]
queue.append('A')
queue.append('B')
queue.append('C')
print("queue:",queue)
#peek
frontElement=queue
print("peek:",frontElement)
#dequeue
poppedElement=queue.pop(0)
print("dequeue:",poppedElement)
print("Queue  aftyer Dequeue:",queue)
#isEmpty
isEmpty=not bool(queue)
print("isEmpty:",isEmpty)
#size
print("size:",len(queue))
