// 3. 여러 줄의 값들을 입력받을 때
const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n");
/*
0 : 빈칸
1 : 집
2 : 치킨집
치킨거리 : 집이랑 가장 가까운 치킨집 까지의 거리
도시의 치킨거리 : 모든 집의 치킨 거리의 합
치킨거리 구하는 공식 : (x,y)  (a,b)    |x-a| + |y-b|
N : N*N 크기의 map
M : 유지할 치킨집의 갯수.
M개의 치킨집을 살려두고, 그때 도시의 치킨거리 (각 가정집에서 구한 치킨거리의 합)
전체 치킨집중 M개의 치킨집을 고르는 경우의 수마다의 새로운 map만들기
*/
[N, M] = input.shift().split(" ").map(Number);
let board = [];
for (let str of input) {
  let temp = str.split(" ").map(Number);
  board.push(temp);
}
let chickens = [];
let homes = [];
let ans = Infinity;
for (let i = 0; i < N; i++) {
  for (let j = 0; j < N; j++) {
    if (board[i][j] == 2) {
      chickens.push([i, j]);
    }
    if (board[i][j] == 1) {
      homes.push([i, j]);
    }
  }
}
const chickenDistance = (chicken, home) => {
  let total = 0;
  for (let i = 0; i < home.length; i++) {
    let min = Infinity;
    let [x, y] = home[i];
    for (let j = 0; j < chicken.length; j++) {
      let [nx, ny] = chicken[j];
      let distance = Math.abs(x - nx) + Math.abs(y - ny);
      min = Math.min(min, distance);
    }
    total += min;
  }
  return total;
};

const DFS = (arr, depth, startIndex) => {
  //종료조건
  if (depth == M) {
    ans = Math.min(chickenDistance(arr, homes), ans);
    return;
  }
  for (let i = startIndex; i < chickens.length; i++) {
    DFS([...arr, chickens[i]], depth + 1, i + 1);
  }
};

DFS([], 0, 0);
console.log(ans);
