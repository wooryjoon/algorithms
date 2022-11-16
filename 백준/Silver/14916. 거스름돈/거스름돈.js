const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim();

const solution = (N) => {
  let answer = 0;
  // if 5로 최대한 나눴을 때 나머지가 홀수이면 nFive를 -1해준다
  // else nFive 그대로 유지.
  // N = N- nFive 로 바꾸고 N을 2로 나눠준다.
  // 예외사항 : 1,3 일때는 거스름돈을 줄 수가 없으므로 -1을 반환하게 한다.
  if (N == "1" || N == "3") return -1;

  let nFive = parseInt(N / 5);
  let rest = N % 5;

  if (rest % 2 == 1) nFive--;
  N = N - 5 * nFive;

  return nFive + parseInt(N / 2);
};

console.log(solution(input));
