const [str1, ...str2] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");
/*
1. 무조건 서로 다른 k개를 연속으로 먹는게 좋다
2. 그중에서도 쿠폰번호가 안껴있는 경우로 고르는게 좋다
3. 
*/
let [N, d, k, c] = str1.split(" ").map(Number); // 접시갯수,초밥가지수,연속몇개,쿠폰
let sushi = []; // 스시배열
let visited = Array(d + 1).fill(0);
let max_sushi = 0;
let eaten = 1;
for (let str of str2) {
  sushi.push(Number(str));
}

visited[c] = 1; // 보너스초밥 먼저 처리
for (let i = 0; i < k; i++) { // 투포인터 돌리기 전 초기값 세팅
  if (visited[sushi[i % N]] === 0) eaten++;
  visited[sushi[i % N]]++;
}
max_sushi = eaten; 

for (let start = 0; start < N; start++) {
  let start_s = sushi[start % N]; // 빼줄 초밥
  let last_s = sushi[(start + k) % N]; // 더해줄 초밥
  visited[start_s]--;
  if (visited[start_s] === 0) eaten--;

  if (visited[last_s] === 0) eaten++;
  visited[last_s]++;
  max_sushi = Math.max(max_sushi, eaten);
}
console.log(max_sushi);
