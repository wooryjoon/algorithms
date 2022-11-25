let [n, ...arr] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

let N = Number(n);
let connect = [];
for (let i = 0; i < arr.length; i++) {
  connect.push(arr[i].split(" ").map(Number));
}

let graph = [...Array(N + 1)].map((e) => []);

for (let i = 0; i < connect.length; i++) {
  let [from, to] = connect[i];
  graph[from].push(to);
  graph[to].push(from);
}
//BFS로 풀기
let answer = [];
let visited = [];
const BFS = (start) => {
  let queue = [];

  queue.push(start);
  visited.push(start);

  while (queue.length !== 0) {
    let currNode = queue.shift();

    for (let i = 0; i < graph[currNode].length; i++) {
      let child = graph[currNode][i];
      if (answer[child]) continue;

      queue.push(child);
      answer[child] = currNode;
    }
  }
};
BFS(1);
let str = "";
for (let i = 2; i <= N; i++) {
  str = str + answer[i] + " ";
}
console.log(str.trim());
