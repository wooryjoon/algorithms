function solution(tickets) {
    // 그래프부터 만들기.
    // 항공권을 모두 사용해야함 -> 프로퍼티의 배열을 사용했으면 -1로 바꾼다.
    let graph = {};
    let ways = [];
    let answer = [];
    
    for (let i = 0; i < tickets.length; i++){
    let key = tickets[i][0];
        graph[key] = [];
    }
    for (let i = 0; i < tickets.length; i++){
    let [from,to] = tickets[i];
        graph[from].push(to);
    }
    for (let [key,value] of Object.entries(graph)) {
        value.sort();
    }; 
    
    const DFS = (node,graph,level) => {
        //종료조건
        if (level == tickets.length+1) {
            answer.push([...ways]);
        };
        // 수행연산
        if (graph[node]) {
            for (let i = 0; i < graph[node].length; i++){
                let child = graph[node][i];
                if (child !== false){ // 아직 안 쓴 티켓
                    graph[node][i] = false;
                    ways.push(child);
                    let flag = DFS(child,graph,level+1);
                    graph[node][i] = child;
                    ways.pop();
                }
            }
        }
    }
    
    ways.push('ICN');
    DFS('ICN',graph,1);
    return (answer[0]);
}