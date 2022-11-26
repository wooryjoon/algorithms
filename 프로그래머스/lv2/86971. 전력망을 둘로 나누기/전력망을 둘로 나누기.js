function solution(n, wires) {
  // wires의 각 항을 반복문하면서 그안에서 BFS 돌리기.
  // ex ) [1,3] 이면, graph에서 1,3을 visited처리하고  개수찾기.

  let graph = [...new Array(n + 1)].map((e) => []);
  let answer = [];
  let visited = new Array(n+1).fill(false);
    
  const BFS = (startNode,visited) => {
    let visit  = [...visited];
    let queue = [startNode];
      let count = 1;
    while (queue.length !== 0) {
      let Node = queue.shift();
      for (let i = 0; i < graph[Node].length; i++) {
        let child = graph[Node][i];
        if ((visit[child] == true)) continue;
        queue.push(child);
        visit[child] = true;
        count++;
      }
    }
    return Math.abs((n- 2*count));
  };

  for (let i = 0; i < wires.length; i++) {
    // 그래프 완성
    let [from, to] = wires[i];
    graph[from].push(to);
    graph[to].push(from);
  }
  wires.forEach((e) => {
    let [a, b] = e;
    visited[a] = true;
    visited[b] = true;
    answer.push(BFS(a,visited));
    visited[a] = false;
    visited[b] = false;
      console.log(visited);
  });
  return Math.min(...answer);
}


