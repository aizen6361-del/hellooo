function convertNumber(num) {
    console.log("Original Number:", num);
    console.log("Decimal:", num.toString(10));
    console.log("Hexadecimal:", num.toString(16));
    console.log("Binary:", num.toString(2));
    console.log("Octal:", num.toString(8));
}
let number = 255;
convertNumber(number);
console.log("Hello World");
export {};
