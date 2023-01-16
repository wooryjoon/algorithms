const [str1, str2] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");
let [n, k] = str1.split(" ").map(Number);
let arr = str2.split(" ").map(Number);
/*
풀이 아이디어)
① 처음에는, "홀수 삭제"를 할 때 홀수 리스트를 모두 받아서 그 개수가 n개라면 2^n 개의 경우를 모두 생각해야 하나?? 라고 생각했는데, 그럴 필요가 없는 것이 연속되게 홀수를 삭제하지 않으면 부분수열이 쭉 짝수가 아니게 되므로 그냥 "연속된 홀수"를 따지면 됨

② 각 포인터에 대해 "홀수" 라면 count(홀수 카운트)를 +1 해주고, "짝수" 라면 tmp(부분수열 길이) 를 +1 한다.

③ 만약 start = 0 부터 end = N 까지 돌았을 때도 홀수 개수가 K개를 넘지 않는다면, 바로 전체 짝수 부분 수열 길이를 출력

④ start 포인터 한 칸 뒤로 옮기기 전 start 값이 "홀수" 라면 count -1(홀수 카운트), "짝수"라면 tmp -1(부분수열 길이 -1)

⑤ while 문 탈출 기준이 count == K 가 아니라 count == K+1 이 되었을 때인데, 이는 예를 들어 K=2라면, 2개를 지우고 3개 째 지울 수 없을 때의 짝수 부분 수열 길이를 출력해야 되기 때문
1 2 3 4 5 5 7 8
*/

let end = 0;
let count = 0;
let length = 0;
let result = 0;
for (let start = 0; start < n; start++) {
  while (count <= k && end < n) {
    if (arr[end] % 2 === 1) count++;
    else length++;
    end++;

    if (start === 0 && end === n) {
      result = length;
      break;
    }
  }
  if (count === k + 1) {
    result = Math.max(result, length);
  }
  if (arr[start] % 2 === 1) {
    count--;
  } else length--;
}
console.log(result);
