const fs = require("fs");

const input1 = fs.readFileSync("/dev/stdin").toString().split(" ");

let A = Number(input1[0]);
let B = Number(input1[1]);
console.log(A + B);
console.log(A - B);
console.log(A * B);
console.log(Math.floor(A / B));
console.log(A % B);
