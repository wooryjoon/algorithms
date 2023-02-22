const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n");

[x, y, w, h] = input[0].trim().split(" ").map(Number);

arr = []
arr.push(y)
arr.push(h-y)
arr.push(w-x)
arr.push(x)
console.log(Math.min(...arr))
