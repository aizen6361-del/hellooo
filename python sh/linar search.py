def Linear_Search(arr , key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
        return -1
mylist = [ 7 , 8 , 2 , 4 , 7 , 9 ]
x = 9
result = Linear_Search(mylist ,  x)
if result != -1:
    print("found at index:",result)
else:
    print("not found")

