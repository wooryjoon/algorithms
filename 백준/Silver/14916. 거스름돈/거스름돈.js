const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim();

const solution = (N) => {
  let answer = 0;
  // 1, 3 예외처리 따로 해주기, 나머지는 그대로.
  if (N == "1" || N == "3") return -1;
  if (N == "6") return 3;
  if (N == "8") return 4;
  else if (
    N[N.length - 1] == "1" ||
    N[N.length - 1] == "3" ||
    N[N.length - 1] == "6" ||
    N[N.length - 1] == "8"
  ) {
    answer += Math.floor(N / 5) - 1;
    N = N - answer * 5;
    answer += Math.floor(N / 2);
  } else {
    answer += Math.floor(N / 5);
    N = N % 5;
    answer += Math.floor(N / 2);
  }
  return answer;
};

console.log(solution(input));
