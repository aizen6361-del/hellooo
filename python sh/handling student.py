class student:
 def __init__(self, name, rollno, m1, m2):
     
  self.name=name
  self.rollno=rollno
  self.m1=m1
  self.m2=m2
 def accept(self, name, rollno, marks1, marks2):
   ob=student(name, rollno, marks1, marks2)
   ls.append(ob)
 def display(self, ob):
     print("Name :", ob.name)
     print("Rollno :", ob.rollno)
     print("Marks1 :", ob.m1)
     print("Marks2 :", ob.m2)
     print("\n")
 def search(self, rn):
     for i in range(ls.__len__()):
         if(ls[i].rollno==rn):
             return i
 def delete(self, rn):
     i=obj.search(rn)
     del ls[i]
 def update(self, rn, no):
     i=obj.search(rn)
     roll=no
     ls[i].rollno=roll;
     ls=[]
     obj=student(' ',0,0,0)
     print("\nOperations used, ")
     print("\n1.accept student details\n2.display student details\n"
"3.search details of a student\n4.delete details of student"
"\n5.update student details\n6.exit")
print("1-->ACCEPT")
obj.accept("A", 1, 100, 100)
obj.accept("B", 2, 90, 90)
obj.accept("C", 3, 80, 80)
print("press any key to continue...")
input()
print("2-->DISPLAY")
print("press any key to continue...")
input()
print("\n")
print("\nlist of student\n")
for i in range(ls.__len__()):
    obj.display(ls[i])
    print("3-->SEARCH")
    print("press any key to continue...")
    input()
    print("\n student found,")
    s=obj.search(2)
    obj.display(ls[s])
    print("4-->DELETE")
print("press any key to continue...")
input()
obj.delete(2)
print(ls.__len__())
print("list after deletion")
for i in range(ls.__len__()):
    obj.display(ls[i])
print("5-->UPDATE")
print("press any key to continue...")
input()
obj.update(3,2)
print(ls.__len__())
print("list after updation")
for i in range(ls.__len__()):
    obj.display(ls[i])
print("6-->EXIT")
prinSt("press any key to continue...")
input()
print("Thank you !")
