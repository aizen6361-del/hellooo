class queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,element):
        self.queue.append(element)
    def dequeue(self):
         if self.isEmpty():
             return "Queue isEmpty"
         return  self.queue.pop(0)
    def peek(self):
         if self.isEmpty():
             return "Queue isEmpty"
         return  self.queue[0]
    def isEmpty(self):
        return  len(self.queue)==0
    
    def size(self):
         return  len(self.queue)
myqueue=queue()
#myqueue.enqueue('A')
#myqueue.enqueue('B')
n=int(input("enter how many elements:"))
for i in range(n):
    item=input("enter the item")
myqueue.enqueue(item)
myqueue
print("queue:",myqueue.queue)
print("peek:",myqueue.peek())
print("dequeue:",myqueue.dequeue())
print("queue after dequeue:",myqueue.isEmpty())
print("size:",myqueue.size())
