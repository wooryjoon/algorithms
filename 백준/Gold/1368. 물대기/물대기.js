const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n");
function find_parent(parents, a) {
  if (parents[a] != a) {
    parents[a] = find_parent(parents, parents[a]);
  }
  return parents[a];
}
function union_parent(parents, a, b) {
  x = find_parent(parents, a);
  y = find_parent(parents, b);
  if (x < y) {
    parents[y] = x;
  } else {
    parents[x] = y;
  }
}
let N = Number(input[0]);
let price = [];
let board = [];
let edges = [];
let parent = Array(N + 2)
  .fill(0)
  .map((e, i) => i);
let ans = 0;
for (let i = 1; i < N + 1; i++) {
  edges.push([Number(input[i]), i, N + 1]);
}
for (let i = N + 1; i <= 2 * N; i++) {
  let temp = input[i].split(" ").map(Number);
  board.push(temp);
}
for (let i = 0; i < board.length; i++) {
  for (let j = 0; j < board[0].length; j++) {
    if (i == j) continue;
    edges.push([board[i][j], i + 1, j + 1]); // 코스트,노드2개
  }
}
edges.sort((a, b) => {
  return a[0] - b[0];
});
let cnt = 0;
for (let x of edges) {
  let [cost, a, b] = x;
  if (find_parent(parent, a) != find_parent(parent, b)) {
    // 각각 부모가 다르다, 연결해도 사이클 안생긴다
    union_parent(parent, a, b);
    ans += cost;
    cnt++;
  }
  if (cnt === N) break;
}
console.log(ans);