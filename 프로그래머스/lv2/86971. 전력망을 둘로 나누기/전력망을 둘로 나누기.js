function solution(n, wires) {
  // 각 간선이 끊어진 경우의 그래프를 구해야함.
  // 해당 그래프 마다 BFS를 통해 두개로 나뉘어진 그룹의 간선의 개수 구하기.
  // 한 그룹의 노드의 개수를 구하면 나머지 하나는 n - 노드개수 하면되네?
  // 1. 그래프 구현
  // 2. 각 간선이 짤린 경우마다 BFS 돌리기.
  // BFS내에서 값의 쌍을 저장할 배열 만들기.
  // 간선을 삭제한 해당 노드를 출발노드로 시작해서 개수를 구하자.
    
  let graph = [...new Array(n + 1)].map((e) => []);
    let visited = new Array(n+1).fill(false);
    let answer = [];

  for (let i = 0; i < wires.length; i++) {
    // 그래프 완성
    let [from, to] = wires[i];
    graph[from].push(to);
    graph[to].push(from);
  }
  for (let i = 1; i < graph.length; i++) {
    graph[i].sort((a, b) => a - b); // 노드와 연결된 간선을 오름차순으로 정렬.
  }
  const BFS = (startNode, graph) => {
    let visit = new Array(n + 1).fill(false);
    let count = 1;
    let queue = [startNode];
      visit[startNode] = true;
    while (queue.length !== 0) {
      let Node = queue.shift();
      for (let i = 0; i < graph[Node].length; i++) {
        let childs = graph[Node][i];
        if (visit[childs] == true) continue;
        queue.push(childs);
        visit[childs] = true;
          count ++;
      }
    }
    return Math.abs(n- 2*count);
  };
  for (let i = 1; i < graph.length; i++) {
    let currNode = i;
    visited[currNode] = true;

    for (let j = 0; j < graph[currNode].length; j++) {
      let child = graph[currNode][j]; // 현재 노드와 연결된 노드
      if (visited[child] == true) continue;
      graph[currNode].splice(graph[currNode].indexOf(child), 1); // 양방향으로 끊어주기
      graph[child].splice(graph[child].indexOf(currNode), 1); // 양방향으로 끊어주기
      answer.push(BFS(child,graph));
      graph[currNode].unshift(child); // BFS돌리고 양방 붙여주기
      graph[child].unshift(currNode); // BFS 돌리고 양방 붙여주기
    }
  }
    return Math.min(...answer);
    
}


