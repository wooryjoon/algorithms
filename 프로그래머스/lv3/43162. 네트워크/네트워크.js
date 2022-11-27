function solution(n, computers) {
// computers배열을 바탕으로 graph를 만든다.
// 각 노드에서 DFS를 돌리기. 전역에서 반복문 돌리면서 DFS 돌리기.
    
    let graph = [...new Array(n+1)].map(e => []);
    let visited = new Array(n+1).fill(false);
    let count = 0;
    const DFS = (startNode) => {
        visited[startNode] = true;
        for (let i = 0; i < graph[startNode].length; i++){
            let child = graph[startNode][i];
            if (visited[child] == true) continue;
            DFS(child);
        }
    }
    computers.unshift(false);
    for (let i = 1; i < computers.length; i++){
        let connect = computers[i]; // i번 노드와 연결된 노드의 배열
        for (let j = 0; j < connect.length; j++){
            if (i-1 == j) continue; // 자기스스로 연결된 노드는 스킵
            if (connect[j] == 1) { // j번째 노드와 
                graph[i].push(j+1)
            }
        }
    }
    for (let i = 1; i < graph.length; i++){
        if (visited[i] == true) continue;
        count ++;
        DFS(i);
    }
    return count;
}