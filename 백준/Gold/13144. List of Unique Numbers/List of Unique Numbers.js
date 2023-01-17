const [str1, str2] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");
/*
arr에서 1개 이상의 연속한수열을 뽑으면서, 거기 원소들이 다 다른 경우의 수 count
투포인터로 해결 가능할 것 같다.
1 2 3 1 2
          e
check :  3 1 2
1 12 123                    2 3 
2 23 231                    3 1
3 31 312                    1 2
1 12
*/
let n = Number(str1);
let numArr = str2.split(" ").map(Number);
let check = Array(100001).fill(false); // 중복 체크할 배열
let count = 0;
let end = 0;
for (let i = 0; i < n; i++) {
  let start = numArr[i];
  while (end < n) {
    let endValue = numArr[end];
    if (check[endValue] === false) {
      check[endValue] = true;
      end++;
    } else break;
  }
  count += end - i;
  check[start] = false;
}
console.log(count);
