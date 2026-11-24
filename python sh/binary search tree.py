class bst:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None
    def  insert(self,data):
        if self.key is None:
            self.key=data
            return
        if self.key < data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                 self.rchild=bst(data)
        else:
             if self.rchild:
                 self.rchild.insert(data)
             else:
                 self.rchild=bst(data)
    def search(self,data):
        if self.key==data:
            print("node is found")
            return
        if data<self.key:
            if self.child:
                self.lchild.search(data)
            else:
                print("node is not present")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("node not present")
root=bst(None)
list=[20,4,39,4,1,5,6]
for i in list:
    root.insert(i)
root.search(20)
