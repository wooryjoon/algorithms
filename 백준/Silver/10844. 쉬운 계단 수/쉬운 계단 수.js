// 3. 여러 줄의 값들을 입력받을 때
const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");
let N = Number(input[0]);
let bill = 1e9;
let dp = [-1, [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]];
for (let i = 2; i <= N; i++) {
  dp.push([]);
}
for (let i = 2; i <= N; i++) {
  for (let j = 0; j < 10; j++) {
    if (j == 0) dp[i][j] = dp[i - 1][j + 1] % bill;
    else if (j == 9) dp[i][j] = dp[i - 1][j - 1] % bill;
    else dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % bill;
  }
}

console.log(
  dp[N].reduce((acc, cur) => {
    return acc + cur;
  }, 0) % bill
);

