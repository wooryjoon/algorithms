let [str1, ...str2] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

str2 = str2.map((e) => e.trim()).reverse();
let [n, m] = str1.split(" ").map(Number); // 가능인원 , 버튼클릭 순서
let arr = [];
let ans = [];

let set = new Set(str2);

set.forEach((value) => {
  arr.push(value);
});
arr.reverse();
for (let i = 0; i < n; i++) {
  if (!arr[i]) break;
  ans.push(arr[i]);
}
console.log(ans.join("\n"));
