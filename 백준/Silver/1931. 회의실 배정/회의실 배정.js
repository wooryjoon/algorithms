// 3. 여러 줄의 값들을 입력받을 때
const [N, ...input] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");
/*
마감시간 기준 오름차순 정렬
*/
let stack = [];
let arr = input.map((e) => {
  return e.split(" ").map(Number);
});
arr.sort((a, b) => {
  if (a[1] == b[1]) return a[0] - b[0];
  else return a[1] - b[1];
});

stack.push(arr[0][1]);

for (let i = 1; i < arr.length; i++) {
  if (arr[i][0] >= stack[stack.length - 1]) {
    stack.push(arr[i][1]);
  }
}
console.log(stack.length);
