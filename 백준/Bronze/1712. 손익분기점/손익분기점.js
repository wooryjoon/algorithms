let input = require("fs").readFileSync("/dev/stdin").toString().split(" ");

const A = input[0] * 1;
const B = input[1] * 1;
const C = input[2] * 1;

const margin = C - B;

let Q = Math.floor(A / margin) + 1;

margin <= 0 ? (Q = -1) : (Q = Q);

console.log(Q);
