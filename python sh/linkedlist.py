class Node:
    def _init_(self, value):
        self.value = value
        self.next = None
class Stack:
    def _init_(self):
        self.head = None
        self.size = 0
    def push(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        popped_node = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_node.value
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.head.value
    def isEmpty(self):
        return self.size == 0
    def stackSize(self):
        return self.size
    def traverseAndPrint(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.value, end=" -> ")
            currentNode = currentNode.next
        print()
# Driver code
mystack = Stack()
mystack.push('A')
mystack.push('B')
mystack.push('C')
print("Linked list:", end=" ")
mystack.traverseAndPrint()
print("Peek:", mystack.peek())
print("Pop:", mystack.pop())
print("Linked list after Pop:", end=" ")
mystack.traverseAndPrint()
print("isEmpty:", mystack.isEmpty())
print("Size:", mystack.stackSize())
