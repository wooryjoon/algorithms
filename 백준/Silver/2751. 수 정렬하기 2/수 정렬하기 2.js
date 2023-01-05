const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map(Number);

//시간복잡도 이슈, 퀵정렬.
let N = input.shift();
input.sort((a, b) => {
  return a - b;
});
let answer = input.join("\n");
console.log(answer);

