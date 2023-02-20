const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n");

let [N, M] = input[0].split(" ").map(Number);
let graph = Array.from(Array(N + 1), () => []);
let inDegree = Array(N + 1).fill(0);
let queue = [];
let ans = [];
for (let i = 1; i <= M; i++) {
  [length, ...arr] = input[i].split(" ").map(Number);
  for (let j = 0; j < length - 1; j++) {
    graph[arr[j]].push(arr[j + 1]);
    inDegree[arr[j + 1]]++;
  }
}

for (let i = 1; i < N + 1; i++) {
  if (inDegree[i] === 0) {
    queue.push(i); // 진입차수가 0인 노드 번호 삽입
    ans.push(i);
  }
}

while (queue.length) {
  let currNode = queue.shift();
  for (let x of graph[currNode]) {
    inDegree[x]--;
    if (inDegree[x] == 0) {
      queue.push(x);
      ans.push(x);
    }
  }
}
if (ans.length != N) {
  console.log(0);
  return;
} else {
  console.log(ans.join("\n"));
  return;
}
