const [n, ...arr] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split(/\s/);

//그냥 오름차순 정렬?
const solution = (k, arr2) => {
  let answer = 0;
  arr2.sort((a, b) => a - b); // [1,2,3,4,5]

  for (let i = 0; i < k; i++) {
    for (let j = 0; j <= i; j++) {
      answer += Number(arr2[j]);
    }
  }
  return answer;
};

console.log(solution(Number(n), arr));
