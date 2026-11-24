class node:
    def __init__(self,data):
        self.key=data
        self.lchild=None
        self.rchild=None
    def insert(self,data):
        if self.key is None:
            self.key=data
            return
        if self.key >=data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild=node(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild=node(data)
    def min_node(self):
        current=self
        while current.lchild:
            current=current.lchild
        print("min node=",current.key)
    def max_node(self):
        current=self
        while current.rchild:
            current=current.rchild
        print("max node=",current.key)
root=node(None)
list1 = [32,15,68,98,60]
for i in list1:
    root.insert(i)
root.min_node()
root.max_node()
