"use strict";
// numberMethods.ts
let num = 123.456;
// using number methods
console.log("original number:", num);
console.log("toFixed(2):", num.toFixed(2));
console.log("toExponential(3):", num.toExponential(3));
console.log("toPrecision(4):", num.toPrecision(4));
console.log("toString():", num.toString());
console.log("valueOf():", num.valueOf());
// static methods from Number class
console.log("Number.isFinite(num):", Number.isFinite(num));
console.log("Number.isInteger(num):", Number.isInteger(num));
console.log("Number.parseInt('123.45'):", Number.parseInt("123.45"));
console.log("Number.parseFloat('123.45'):", Number.parseFloat("123.45"));
console.log("Number.isNaN(NaN):", Number.isNaN(NaN));
