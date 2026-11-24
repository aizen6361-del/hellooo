stack=[]
def push():
    item=input("enter the item to be pushed")
    stack.append(item)
    print(stack)
def pop():
    if not stack:
        print("stack is empty")
    else:
        e=stack.pop()
    print("the element poped is =",e)
true=1
while true:
    print("1.push 2.pop 3.exit")
    ch=int(input("enter the choice"))
    if(ch==1):
        push()
    elif(ch==2):
        pop()
    elif(ch==3):
        break
    else:
        print("enter the correct choice")
