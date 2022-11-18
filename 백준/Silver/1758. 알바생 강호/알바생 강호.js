const [n, ...arr] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

//1등 -> 가격그대로 팁을 줘
//음수라면 팁못받음.
//팁 많이주려는 놈을 앞에 세우는게 이득

const solution = (k, arr2) => {
  arr2.sort((a, b) => b - a); // 내림차순 정렬
  let answer = 0;

  for (let i = 0; i < k; i++) {
    if (arr2[i] - i >= 0) {
      answer += arr2[i] - i;
    }
  }
  return answer;
};

console.log(solution(n, arr));
