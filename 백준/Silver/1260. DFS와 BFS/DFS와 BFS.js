const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

let arr = input[0].split(" ").map(Number);
let nodeLength = arr[0];
let lines = arr[1];
let first = arr[2];
let connect = [];

// let arr = [4, 5, 1];
// let nodeLength = arr[0];
// let lines = arr[1];
// let first = arr[2];
// let connect = [
//   [1, 2],
//   [1, 3],
//   [1, 4],
//   [2, 4],
//   [3, 3],
// ];

for (let i = 1; i <= lines; i++) {
  connect.push(input[i].split(" ").map(Number));
}
let graph = [...Array(nodeLength + 1)].map((e) => []);
let visited = [];

for (let i = 0; i < lines; i++) {
  let [from, to] = connect[i];
  graph[from].push(to);
  graph[to].push(from);
}

const DFS = (start) => {
  visited.push(start);
  graph[start].sort((a, b) => a - b);
  for (let i = 0; i < graph[start].length; i++) {
    let node = graph[start][i];
    if (!visited.includes(node)) {
      DFS(node);
    }
  }
};
const BFS = (start) => {
  let queue = []; // 선입선출
  queue.push(start);
  visited.push(start);
  while (queue.length !== 0) {
    let currNode = queue.shift();
    graph[currNode].sort((a, b) => a - b);
    for (let i = 0; i < graph[currNode].length; i++) {
      if (!visited.includes(graph[currNode][i])) {
        queue.push(graph[currNode][i]);
        visited.push(graph[currNode][i]);
      }
    }
  }
};
DFS(first);
console.log(visited.join(" "));
visited = [];
BFS(first);
console.log(visited.join(" "));
