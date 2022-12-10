function solution(n, edge) {
    // map 만들고 bfs로 노드마다 걸리는 시간 체크.
    let maps = Array.from(Array(n+1), () => Array());
    let visited = Array(n+1).fill(false);
    let answer = 0;
    
    const BFS = ([startNode,count]) => {
        let queue = [];
        visited[startNode] = 0;
        queue.push([startNode,count]);
        while (queue.length){
            let [currNode,count] = queue.shift();
            for (let i = 0; i < maps[currNode].length; i++){
                let sibling = maps[currNode][i];
                if (visited[sibling] === false){
                    queue.push([sibling,count+1]);
                    visited[sibling] = count+1;
                }
            }
        }
    }
    for (let i = 0; i < edge.length; i++){
        let [from,to] = edge[i];
        maps[from].push(to);
        maps[to].push(from);
    }
    BFS([1,0]);
    let max = Math.max(...visited);
    for (let e of visited){
        if (e === max) answer ++;
    }
    return answer;
}