let numbers = [10, 20, 30];
console.log("Original Array:", numbers);
// Adding elements using push()
numbers.push(40);
numbers.push(50);
console.log("After push (40,50):", numbers);
// Removing elements using pop()
let removedElement1 = numbers.pop();
console.log("After pop():", numbers, "|Removed:", removedElement1);
let removedElement2 = numbers.pop();
console.log("After another pop():", numbers, "|Removed:", removedElement2);
export {};
