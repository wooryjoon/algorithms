const [str1, str2] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

let [n, k] = str1.split(" ").map(Number); // 배열 길이, k : 중복 가능횟수
let numArr = str2.split(" ").map(Number);
let end = 0;
let visited = Array(100010).fill(0);
let result = 0;
let length = 0;
/* 

*/
for (let start = 0; start < n; start++) {
  while (end < n) {
    let value = numArr[end];
    if (visited[value] < k) {
      visited[value]++;
      length++;
    } else if (visited[value] >= k) break;
    end++;
  }
  result = Math.max(result, length);
  visited[numArr[start]]--;
  length--;
}
console.log(result);
