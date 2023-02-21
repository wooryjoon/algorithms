//다익스트라 알고리즘 구현

/*
각 노드간 최단거리를 모두 구한다
n번부터 1,2,3,4,n,5,6,..까지의 최단거리를 바탕으로
탐색범위 내에 들어가는 것들은 아이템 획득시키기
무방향인지 단방향인지 확인 잘하기.
*/

const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n");

[n, m, r] = input[0].split(" ").map(Number); // 지역,수색범위,길개수
let items = input[1].split(" ").map(Number);
items.unshift(-1);

let graph = Array.from(Array(n + 1), () => Array(n + 1).fill(Infinity));
let ans = -10000;
for (let i = 2; i < r + 2; i++) {
  [start, to, dist] = input[i].split(" ").map(Number);
  graph[start][to] = dist;
  graph[to][start] = dist;
}
for (let x = 1; x < n + 1; x++) {
  for (let y = 1; y < n + 1; y++) {
    if (x === y) {
      graph[x][y] = 0;
    }
  }
}
for (let k = 1; k < n + 1; k++) {
  for (let x = 1; x < n + 1; x++) {
    for (let y = 1; y < n + 1; y++) {
      graph[x][y] = Math.min(graph[x][y], graph[x][k] + graph[k][y]);
    }
  }
}
for (let x = 1; x < n + 1; x++) {
  temp = 0;
  for (let y = 1; y < n + 1; y++) {
    if (graph[x][y] <= m) {
      temp += items[y];
    }
  }
  ans = Math.max(ans, temp);
}
console.log(ans);
