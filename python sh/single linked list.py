class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class sll:
    def __init__(self):
        self.head = None
    def sl(self):
        n1 = node(10)
        self.head = n1
        n2 = node(20)
        n1.next = n2
    def display(self):
        temp = self.head
        if self.head is None:
            print("empty")
        while temp:
            print(temp.data)
            temp = temp.next
nap=node(10)
nap= sll()
nap.sl()
nap.display()
