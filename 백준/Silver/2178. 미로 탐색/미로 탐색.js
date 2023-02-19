/*
문제 정리
    1 : 이동가능
    0 : 이동 불가능
    (1,1) 에서 출발
    끝까지 이동
    지나야 하는 최소 칸 수
    칸을 셀 떄는 시작 위치와 도착 위치도 포함
아이디어
    BFS탐색을 통해서, 갈 수 있는 칸이면 현재칸 + 1
    n,m에 도달했을 때 그떄의 값 출력
*/

const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n");

[n, m] = input[0].split(" ").map(Number);
maze = [];
visited = Array.from(Array(n), () => Array(m).fill(false));
for (let i = 1; i <= n; i++) {
  maze.push([...input[i]].map(Number));
}
dx = [0, 0, 1, -1];
dy = [1, -1, 0, 0];
function BFS(i, j) {
  let queue = [];
  queue.push([i, j, 1]);
  visited[i][j] = true;
  while (queue.length) {
    [x, y, count] = queue.shift();
    if (x === n - 1 && y === m - 1) {
      return count;
    }
    for (let i = 0; i < 4; i++) {
      [nx, ny] = [x + dx[i], y + dy[i]];
      if (
        nx >= 0 &&
        nx < n &&
        ny >= 0 &&
        ny < m &&
        visited[nx][ny] === false &&
        maze[nx][ny] === 1
      ) {
        visited[nx][ny] = true;
        queue.push([nx, ny, count + 1]);
      }
    }
  }
}
console.log(BFS(0, 0));

