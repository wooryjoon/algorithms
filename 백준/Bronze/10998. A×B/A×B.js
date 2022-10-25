const fs = require("fs");

const input1 = fs.readFileSync("/dev/stdin").toString().split(" ");

let A = input1[0];
let B = input1[1];

console.log(A * B);
