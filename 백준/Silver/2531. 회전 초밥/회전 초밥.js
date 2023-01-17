const [str1, ...str2] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

let [N, d, k, c] = str1.split(" ").map(Number); // 접시수,가짓수,몇연속, 보너스
let belt = [];
let eaten = 0;
let count = 0;
let result = 0;
for (let s of str2) {
  belt.push(Number(s));
}
let visited = Array(d + 10).fill(0); // 중복 체크 배열
visited[c] = 1;
eaten = 1;

while (count < k) {
  // 첫 초밥 세팅
  let sushi = belt[count];
  if (visited[sushi] === 0) {
    eaten++;
  }
  visited[sushi]++;
  count++;
}

for (let i = 0; i < N; i++) {
  let start_s = belt[i];
  let next_s = belt[(i + k) % N];

  visited[start_s]--;
  if (visited[start_s] === 0) eaten--;

  if (visited[next_s] === 0) eaten++;
  visited[next_s]++;

  result = Math.max(eaten, result);
}
console.log(result);
