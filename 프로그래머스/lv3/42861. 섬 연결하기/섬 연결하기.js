function solution(n, costs) {
    // 유니온 파인드를 기반으로 한 크루스칼 알고리즘.
    let parents = Array(n).fill(0).map((e,i) => i);
    let answer = 0;
    const getParent = (parent,x) => {
        if (parent[x] == x) return x;
        return parent[x] = getParent(parent,parent[x]);
    }
    const unionParent = (parent,a,b) => {
        a = getParent(parent,a); // a의 부모찾기
        b = getParent(parent,b); // b의 부모찾기
        if (a > b) parent[a] = b;
        else parent[b] = a;
    }
    costs.sort((a,b) => {
        return a[2] -b[2];
    })
    
    for (let i = 0; i < costs.length; i++){
        let [from,to,price] = costs[i];
        if (getParent(parents,from) != getParent(parents,to)){ // 서로 각자 다른 부모 노드를 가지면
            answer += price;
            unionParent(parents,from,to); // 서로 같은 부모를 갖도록 합쳐주기
        } // 만약 모두가 같은 부모를 가진다면 (모두 연결) for문이 더이상 연산 없이 for문 종료됨.
    }
    return answer;
    
    

    
}