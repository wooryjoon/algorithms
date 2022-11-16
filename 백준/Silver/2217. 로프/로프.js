let [n, ...arr] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");
arr = arr.map((a) => parseInt(a));
arr.sort((a, b) => a - b); // 오름차순 정렬 // 원소를 숫자 타입으로 변경

let max = 0;
let temp = 0;
for (let i = 0; i < arr.length; i++) {
  temp = arr[i] * (arr.length - i);
  max = Math.max(max, temp);
}
console.log(max);